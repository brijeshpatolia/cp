// A TCP proxy in front of Postgres that reads the wire protocol, to check that the app
// never pipelines: sends another query on a connection that still owes it a reply.
// With `supavisor: true` it also treats a pipelining client the way Supabase's pooler
// (Supavisor 2.9, transaction mode) does: it delivers one more reply and then nothing,
// so the client waits forever (supabase/supavisor#1239). Plain TCP only, no TLS.
import net from "node:net";

export type WireProxy = {
  url: string;
  stats: { connections: number; pipelined: number; stalled: number };
  // Every open connection stops answering, as if its socket had died; new ones work.
  stallAll(): void;
  close(): Promise<void>;
};

// Splits a byte stream into protocol messages and passes on, in one write per chunk
// received, the ones `keep` returns true for. The first message from a client (the
// startup packet) has no type byte; it is reported with type "".
function messages(startup: boolean, keep: (type: string, message: Buffer) => boolean, write: (data: Buffer) => void) {
  let buffered: Buffer = Buffer.alloc(0);
  return (chunk: Buffer) => {
    buffered = buffered.length ? Buffer.concat([buffered, chunk]) : chunk;
    const out: Buffer[] = [];
    for (;;) {
      const typeBytes = startup ? 0 : 1;
      if (buffered.length < typeBytes + 4) break;
      const size = typeBytes + buffered.readInt32BE(typeBytes);
      if (buffered.length < size) break;
      const message = buffered.subarray(0, size);
      buffered = buffered.subarray(size);
      if (keep(startup ? "" : String.fromCharCode(message[0]), message)) out.push(message);
      startup = false;
    }
    if (out.length) write(Buffer.concat(out));
  };
}

// `target` is a postgres:// URL; the returned `url` is the same database through the proxy.
export async function startWireProxy(target: string, opts: { supavisor?: boolean } = {}): Promise<WireProxy> {
  const to = new URL(target);
  const stats = { connections: 0, pipelined: 0, stalled: 0 };
  const sockets = new Set<net.Socket>();
  const stallers = new Set<() => void>();

  const server = net.createServer((client) => {
    stats.connections++;
    const upstream = net.connect(Number(to.port || 5432), to.hostname);
    for (const s of [client, upstream]) {
      s.setNoDelay(true);
      sockets.add(s);
      s.on("close", () => sockets.delete(s));
      s.on("error", () => {});
    }
    client.on("close", () => upstream.destroy());
    upstream.on("close", () => client.destroy());

    let owed = 0; // replies the client is waiting for: one per startup, Sync or simple Query
    let idle = false; // no transaction open, as of the last ReadyForQuery
    let stallAfterReply = false;
    let stalled = false;
    const stall = () => {
      if (!stalled) stats.stalled++;
      stalled = true;
    };
    stallers.add(stall);
    client.on("close", () => stallers.delete(stall));

    client.on(
      "data",
      messages(true, (type) => {
        // Password messages answer the server, and Terminate needs no reply.
        if (owed > 0 && type !== "p" && type !== "X") {
          stats.pipelined++;
          if (opts.supavisor && idle) stallAfterReply = true;
        }
        if (type === "" || type === "S" || type === "Q") owed++;
        return true;
      }, (data) => upstream.write(data)),
    );

    upstream.on(
      "data",
      messages(false, (type, message) => {
        if (stalled) return false;
        if (type === "Z") {
          owed--;
          idle = message[5] === 0x49; // 'I'
          if (stallAfterReply) stall(); // this reply still goes out; nothing after it
        }
        return true;
      }, (data) => client.write(data)),
    );
  });

  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  const via = new URL(target);
  via.hostname = "127.0.0.1";
  via.port = String((server.address() as net.AddressInfo).port);

  return {
    url: via.toString(),
    stats,
    stallAll: () => stallers.forEach((stall) => stall()),
    close: () =>
      new Promise<void>((resolve) => {
        for (const s of sockets) s.destroy();
        server.close(() => resolve());
      }),
  };
}

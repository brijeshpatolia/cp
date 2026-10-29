// Diwali decorations: marigold toran, diya, rangoli. Pure SVG/CSS, no image files.
import { useId, type CSSProperties } from "react";

// One tile of the garland: a string with an orange and a yellow marigold and a
// mango leaf between them. Tiles repeat horizontally and scale with the height.
const PETALS: [number, number][] = Array.from({ length: 10 }, (_, i) => {
  const a = (i * Math.PI) / 5;
  return [Number((6 * Math.cos(a)).toFixed(2)), Number((6 * Math.sin(a)).toFixed(2))];
});

function marigold(x: number, petal: string, centre: string) {
  const petals = PETALS.map(([cx, cy]) => `<circle cx='${cx}' cy='${cy}' r='3.5' fill='${petal}'/>`).join("");
  return `<path d='M${x} 3V13' stroke='#92400e' stroke-width='1.2'/>
    <g transform='translate(${x} 22)'>${petals}<circle r='4.6' fill='${centre}'/><circle cx='-1.2' cy='-1.2' r='1.6' fill='#fef3c7' opacity='.8'/></g>`;
}

const TORAN_TILE = `<svg xmlns='http://www.w3.org/2000/svg' width='64' height='34' viewBox='0 0 64 34'>
  <path d='M0 3H64' stroke='#92400e' stroke-width='2'/>
  ${marigold(16, "#f97316", "#c2410c")}
  ${marigold(48, "#fbbf24", "#d97706")}
  <g transform='translate(32 3)'>
    <path d='M0 0C4.5 5 4.5 14 0 19C-4.5 14-4.5 5 0 0Z' fill='#15803d'/>
    <path d='M0 2V17' stroke='#86efac' stroke-width='.8'/>
  </g>
</svg>`;

const TORAN_URL = `url("data:image/svg+xml;utf8,${encodeURIComponent(TORAN_TILE)}")`;

// A marigold garland across the top of a screen. Height sets the scale.
export function Toran({ className = "h-8" }: { className?: string }) {
  return (
    <div
      aria-hidden
      className={`pointer-events-none w-full shrink-0 ${className}`}
      style={{ backgroundImage: TORAN_URL, backgroundRepeat: "repeat-x", backgroundSize: "auto 100%" }}
    />
  );
}

// A clay lamp with a flickering flame.
export function Diya({ className = "h-10 w-10" }: { className?: string }) {
  const id = useId();
  return (
    <svg viewBox="0 0 64 64" className={className} aria-hidden>
      <defs>
        <radialGradient id={`${id}g`}>
          <stop offset="0" stopColor="#fde68a" stopOpacity="0.95" />
          <stop offset="1" stopColor="#fde68a" stopOpacity="0" />
        </radialGradient>
        <linearGradient id={`${id}f`} x1="0" y1="1" x2="0" y2="0">
          <stop offset="0" stopColor="#ea580c" />
          <stop offset="0.55" stopColor="#f59e0b" />
          <stop offset="1" stopColor="#fef3c7" />
        </linearGradient>
      </defs>
      <circle className="diya-glow" cx="32" cy="20" r="19" fill={`url(#${id}g)`} />
      <g className="diya-flame">
        <path d="M32 4C38 13 40 21 32 30C24 21 26 13 32 4Z" fill={`url(#${id}f)`} />
        <path d="M32 15C34.5 19 34.5 24 32 28C29.5 24 29.5 19 32 15Z" fill="#fffbeb" />
      </g>
      <path d="M5 33H59C57 47 45 56 32 56C19 56 7 47 5 33Z" fill="#b45309" />
      <path d="M5 33H59" stroke="#78350f" strokeWidth="3.5" strokeLinecap="round" />
      <path d="M14 41Q32 50 50 41" stroke="#fbbf24" strokeWidth="2.6" fill="none" strokeDasharray="0.1 6" strokeLinecap="round" />
    </svg>
  );
}

export function DiyaRow({ count = 5, className = "h-[6vh] w-[6vh]" }: { count?: number; className?: string }) {
  return (
    <div className="flex items-end justify-center gap-[1.5vw]" aria-hidden>
      {Array.from({ length: count }, (_, i) => (
        <span key={i} style={{ "--delay": `${i * -0.37}s` } as CSSProperties} className="inline-block">
          <Diya className={className} />
        </span>
      ))}
    </div>
  );
}

function ring(n: number, r: number, rx: number, ry: number, fill: string, offset = 0) {
  return Array.from({ length: n }, (_, i) => (
    <ellipse key={`${r}-${i}`} cx="100" cy={100 - r} rx={rx} ry={ry} fill={fill} transform={`rotate(${(i * 360) / n + offset} 100 100)`} />
  ));
}

// A rangoli mandala, used as a faint watermark (opacity comes from the theme).
export function Rangoli({ className = "", opacity = "var(--rangoli-opacity)" }: { className?: string; opacity?: string }) {
  return (
    <svg viewBox="0 0 200 200" className={className} aria-hidden style={{ opacity }}>
      {ring(32, 92, 3.2, 3.2, "#0f766e")}
      {ring(16, 74, 9, 17, "#f59e0b", 11.25)}
      {ring(16, 74, 2.6, 2.6, "#fff7ea", 11.25)}
      {ring(12, 50, 8, 16, "#db2777")}
      {ring(8, 29, 7, 13, "#7c3aed", 22.5)}
      <circle cx="100" cy="100" r="15" fill="#fbbf24" />
      <circle cx="100" cy="100" r="7" fill="#ea580c" />
    </svg>
  );
}

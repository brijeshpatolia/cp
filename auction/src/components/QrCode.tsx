"use client";

import QRCode from "qrcode";
import { useEffect, useState } from "react";

// Always dark-on-white with a quiet zone, whatever the page theme, so phones scan it reliably.
export function QrCode({ value, className = "" }: { value: string; className?: string }) {
  const [svg, setSvg] = useState("");
  useEffect(() => {
    if (!value) return;
    QRCode.toString(value, { type: "svg", margin: 2, errorCorrectionLevel: "M", color: { dark: "#111111", light: "#ffffff" } })
      .then(setSvg)
      .catch(() => setSvg(""));
  }, [value]);
  return (
    <div
      className={`aspect-square overflow-hidden rounded-2xl bg-white [&>svg]:h-full [&>svg]:w-full ${className}`}
      role="img"
      aria-label={`QR code for ${value}`}
      dangerouslySetInnerHTML={{ __html: svg }}
    />
  );
}

import type { ButtonHTMLAttributes, ReactNode } from "react";
import type { Level } from "@/lib/levels";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
};

const VARIANTS = {
  primary: "bg-accent text-accent-ink shadow-sm",
  secondary: "border border-line bg-surface text-ink",
  danger: "bg-bad text-white",
  ghost: "text-muted hover:text-ink",
};

const SIZES = {
  sm: "px-3 py-1.5 text-sm",
  md: "px-4 py-2.5",
  lg: "px-5 py-4 text-lg",
};

export function Button({ variant = "primary", size = "md", className = "", type = "button", ...props }: ButtonProps) {
  return (
    <button
      type={type}
      className={`inline-flex items-center justify-center gap-2 rounded-xl font-semibold transition active:scale-[0.98] disabled:pointer-events-none disabled:opacity-40 ${VARIANTS[variant]} ${SIZES[size]} ${className}`}
      {...props}
    />
  );
}

export function Card({ className = "", children }: { className?: string; children: ReactNode }) {
  return <div className={`rounded-2xl border border-line bg-surface p-4 ${className}`}>{children}</div>;
}

export const inputClass =
  "w-full min-w-0 rounded-xl border border-line bg-bg px-3 py-2.5 text-ink outline-none placeholder:text-muted focus:border-accent";

export function Label({ children, htmlFor }: { children: ReactNode; htmlFor?: string }) {
  return (
    <label htmlFor={htmlFor} className="mb-1 block text-sm font-medium text-muted">
      {children}
    </label>
  );
}

const SENIOR: Level[] = ["Director", "MD"];

export function LevelBadge({ level }: { level: Level }) {
  return (
    <span
      className={`inline-block rounded-full px-2 py-0.5 text-xs font-semibold ${
        SENIOR.includes(level) ? "bg-ink text-bg" : "bg-surface-2 text-muted"
      }`}
    >
      {level}
    </span>
  );
}

export function TeamDot({ color, className = "h-3 w-3" }: { color: string; className?: string }) {
  return <span className={`inline-block shrink-0 rounded-full ${className}`} style={{ background: color }} />;
}

export function ErrorText({ children }: { children: ReactNode }) {
  if (!children) return null;
  return <p className="mt-2 text-sm font-medium text-bad">{children}</p>;
}

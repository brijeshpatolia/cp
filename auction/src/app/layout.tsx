import type { Metadata, Viewport } from "next";
import { Geist, Geist_Mono, Yatra_One } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// Festive display face for headings; also covers Devanagari (शुभ दीपावली).
const yatra = Yatra_One({
  variable: "--font-yatra",
  weight: "400",
  subsets: ["latin", "devanagari"],
});

export const metadata: Metadata = {
  title: "Diwali Perks Auction",
  description: "Check in, meet your team, and bid for perks. Happy Diwali!",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fff7ea" },
    { media: "(prefers-color-scheme: dark)", color: "#1b0a1e" },
  ],
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={`${geistSans.variable} ${geistMono.variable} ${yatra.variable} h-full antialiased`}>
      <body className="min-h-full">{children}</body>
    </html>
  );
}

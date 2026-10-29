import type { Metadata } from "next";
import { Board } from "@/components/board/Board";

export const metadata: Metadata = { title: "Big screen · Office Auction" };

export default function BoardPage() {
  return <Board />;
}

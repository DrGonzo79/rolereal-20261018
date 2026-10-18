import type {Metadata} from "next";
import "./globals.css";
export const metadata: Metadata = {title:"RoleReal — Try the shift before the career",description:"Interactive practitioner-authored career simulation prototype."};
export default function RootLayout({children}:{children:React.ReactNode}) { return <html lang="en"><body>{children}</body></html>; }

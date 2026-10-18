import type {NextConfig} from "next";
const repo = "rolereal-20261018";
const isProd = process.env.NODE_ENV === "production";
const config: NextConfig = {output:"export", trailingSlash:true, images:{unoptimized:true}, basePath:isProd?`/${repo}`:"", assetPrefix:isProd?`/${repo}/`:""};
export default config;

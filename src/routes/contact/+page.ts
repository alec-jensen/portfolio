// no imports needed

// This page needs client-side JS for copy buttons even on hard reloads
export const csr = true;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

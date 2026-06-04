// Post-build: inline local SVG <img> sources into deck.html as base64 data URIs,
// so the rendered HTML is a single self-contained file (email it, open it offline).
// Source SVGs stay as separate, editable files in assets/.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';

const HTML = 'deck.html';
let html = readFileSync(HTML, 'utf8');
let count = 0;

html = html.replace(/src="(?:\.\/)?(assets\/[^"]+\.svg)"/g, (match, path) => {
  if (!existsSync(path)) {
    console.warn(`  ! missing asset, left as-is: ${path}`);
    return match;
  }
  const b64 = Buffer.from(readFileSync(path, 'utf8'), 'utf8').toString('base64');
  count++;
  return `src="data:image/svg+xml;base64,${b64}"`;
});

writeFileSync(HTML, html);
console.log(`Inlined ${count} SVG asset(s) into ${HTML} (now self-contained).`);

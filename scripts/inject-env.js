const fs = require('fs');
const path = require('path');
const repoName = process.env.NAME || '';
const base = process.env.PUBLIC_BASE_PATH || (repoName ? `/${repoName}/` : '/');
fs.writeFileSync(path.join(process.cwd(), '.env.local'), `VITE_PUBLIC_BASE_PATH=${base}\n`);
console.log(`Set VITE_PUBLIC_BASE_PATH=${base}`);

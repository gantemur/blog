const fs = require("node:fs");

for (const dir of ["_site", "_tmp"]) {
  fs.rmSync(dir, { recursive: true, force: true });
}

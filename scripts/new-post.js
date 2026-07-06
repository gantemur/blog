#!/usr/bin/env node
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const isPrivateDraft = process.argv.includes("--private-draft");
const title = process.argv.filter((arg) => arg !== "--private-draft").slice(2).join(" ").trim();

if (!title) {
  console.error("Usage: npm run new -- \"Post Title\"");
  console.error("   or: npm run new:draft -- \"Post Title\"");
  process.exit(1);
}

function today() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function slugify(value) {
  const slug = value
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^\p{Letter}\p{Number}\s_-]+/gu, "")
    .trim()
    .replace(/[\s_]+/g, "-")
    .replace(/-+/g, "-");
  return slug || "post";
}

function uniquePath(directory, filename) {
  let candidate = path.join(directory, filename);
  const ext = path.extname(filename);
  const base = filename.slice(0, -ext.length);
  let index = 2;
  while (fs.existsSync(candidate)) {
    candidate = path.join(directory, `${base}-${index}${ext}`);
    index += 1;
  }
  return candidate;
}

const date = today();
const slug = slugify(title);
const directory = isPrivateDraft ? path.join(root, "_private", "drafts") : path.join(root, "src", "posts");
fs.mkdirSync(directory, { recursive: true });

const filePath = uniquePath(directory, `${date}-${slug}.md`);
const body = `---\nlayout: layouts/post.njk\ntitle: ${JSON.stringify(title)}\ndate: ${date}\ntags: []\ncomments: true\ndraft: ${isPrivateDraft ? "true" : "false"}\n---\n\n`;

fs.writeFileSync(filePath, body, "utf8");
console.log(path.relative(root, filePath));

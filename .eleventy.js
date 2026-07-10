const path = require("node:path");

module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });

  const isPublicPost = (item) => {
    return item.data.draft !== true && !["draft", "private"].includes(item.data.status || "");
  };

  const tagSlug = (value) => {
    const normalized = String(value || "")
      .normalize("NFKC")
      .trim()
      .toLowerCase()
      .replace(/\s+/g, "-");
    return encodeURIComponent(normalized).replace(/%2F/gi, "-");
  };

  const escapeHtml = (value) => {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  };

  eleventyConfig.addFilter("readableDate", (value) => {
    return new Intl.DateTimeFormat("en", {
      year: "numeric",
      month: "short",
      day: "numeric"
    }).format(new Date(value));
  });

  eleventyConfig.addFilter("dateIso", (value) => {
    return new Date(value).toISOString();
  });

  eleventyConfig.addFilter("year", (value) => {
    return new Date(value).getFullYear();
  });

  eleventyConfig.addFilter("dateYmd", (value) => {
    const date = new Date(value);
    return [
      date.getFullYear(),
      String(date.getMonth() + 1).padStart(2, "0"),
      String(date.getDate()).padStart(2, "0")
    ].join("-");
  });

  eleventyConfig.addFilter("slugify", (value) => {
    return String(value || "")
      .normalize("NFKD")
      .toLowerCase()
      .replace(/[^\w\s-]/g, "")
      .trim()
      .replace(/[-\s]+/g, "-");
  });

  eleventyConfig.addFilter("tagSlug", (value) => {
    return tagSlug(value);
  });

  eleventyConfig.addFilter("limit", (values, count) => {
    return Array.isArray(values) ? values.slice(0, count) : [];
  });

  eleventyConfig.addFilter("homeExcerpt", (content, fallbackLength = 420) => {
    const html = String(content || "");
    const marker = html.match(/<!--\s*more\s*-->/i);
    if (marker && marker.index > 0) {
      return html.slice(0, marker.index).trim();
    }

    const paragraph = html.match(/<p\b[^>]*>[\s\S]*?<\/p>/i);
    if (paragraph) return paragraph[0];

    const text = html
      .replace(/<script\b[\s\S]*?<\/script>/gi, "")
      .replace(/<style\b[\s\S]*?<\/style>/gi, "")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim();
    if (!text) return "";

    const excerpt = text.length > fallbackLength
      ? `${text.slice(0, fallbackLength).trim()}...`
      : text;
    return `<p>${escapeHtml(excerpt)}</p>`;
  });

  eleventyConfig.addCollection("posts", (collectionApi) => {
    return collectionApi
      .getFilteredByGlob("src/posts/**/*.md")
      .filter(isPublicPost)
      .sort((a, b) => b.date - a.date);
  });

  eleventyConfig.addCollection("postsByYear", (collectionApi) => {
    const grouped = new Map();
    for (const post of collectionApi.getFilteredByGlob("src/posts/**/*.md")) {
      if (!isPublicPost(post)) continue;
      const year = post.date.getFullYear();
      if (!grouped.has(year)) grouped.set(year, []);
      grouped.get(year).push(post);
    }
    return Array.from(grouped.entries())
      .sort((a, b) => b[0] - a[0])
      .map(([year, posts]) => ({ year, posts }));
  });

  eleventyConfig.addCollection("postsByMonth", (collectionApi) => {
    const grouped = new Map();
    for (const post of collectionApi.getFilteredByGlob("src/posts/**/*.md")) {
      if (!isPublicPost(post)) continue;
      const month = `${post.date.getFullYear()}-${String(post.date.getMonth() + 1).padStart(2, "0")}`;
      if (!grouped.has(month)) grouped.set(month, []);
      grouped.get(month).push(post);
    }
    return Array.from(grouped.entries())
      .sort((a, b) => b[0].localeCompare(a[0]))
      .map(([month, posts]) => ({ month, posts }));
  });

  eleventyConfig.addCollection("categoryList", (collectionApi) => {
    const counts = new Map();
    for (const post of collectionApi.getFilteredByGlob("src/posts/**/*.md")) {
      if (!isPublicPost(post)) continue;
      for (const category of post.data.categories || []) {
        const slug = tagSlug(category);
        const existing = counts.get(slug) || { name: category, slug, names: [], count: 0 };
        if (!existing.names.includes(category)) existing.names.push(category);
        existing.count += 1;
        counts.set(slug, existing);
      }
    }
    return Array.from(counts.values())
      .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name, "mn"));
  });

  eleventyConfig.addCollection("tagList", (collectionApi) => {
    const tags = new Set();
    for (const post of collectionApi.getFilteredByGlob("src/posts/**/*.md")) {
      if (!isPublicPost(post)) continue;
      for (const tag of post.data.tags || []) tags.add(tag);
    }
    return Array.from(tags).sort((a, b) => a.localeCompare(b));
  });

  eleventyConfig.addCollection("popularKeywords", (collectionApi) => {
    const counts = new Map();
    for (const post of collectionApi.getFilteredByGlob("src/posts/**/*.md")) {
      if (!isPublicPost(post)) continue;
      for (const tag of post.data.tags || []) {
        counts.set(tag, (counts.get(tag) || 0) + 1);
      }
    }
    return Array.from(counts.entries())
      .map(([name, count]) => ({ name, count }))
      .filter((tag) => tag.count > 1)
      .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name, "mn"))
      .slice(0, 48);
  });

  eleventyConfig.addCollection("topicPages", (collectionApi) => {
    const order = new Map([
      ["contents", 0],
      ["algebr", 1],
      ["geometry", 2],
      ["numbers", 3],
      ["analysis", 4],
      ["topology", 5],
      ["physics", 6],
      ["astronomy", 7],
      ["calendar", 8],
      ["history", 9],
      ["algorithms", 10],
      ["cpp", 11],
      ["logical-fallacies", 12]
    ]);
    return collectionApi
      .getFilteredByGlob("src/pages/**/*.md")
      .filter((item) => item.data.status !== "draft" && item.data.draft !== true)
      .sort((a, b) => {
        const aOrder = order.has(a.data.slug) ? order.get(a.data.slug) : 999;
        const bOrder = order.has(b.data.slug) ? order.get(b.data.slug) : 999;
        return aOrder - bOrder || String(a.data.title).localeCompare(String(b.data.title));
      });
  });

  eleventyConfig.addFilter("postsWithTag", (posts, tag) => {
    return posts.filter((post) => (post.data.tags || []).includes(tag));
  });

  eleventyConfig.addFilter("postsWithCategory", (posts, category) => {
    const names = Array.isArray(category?.names) ? category.names : [category];
    return posts.filter((post) => (post.data.categories || []).some((name) => names.includes(name)));
  });

  eleventyConfig.addShortcode("assetUrl", function (assetPath) {
    const normalized = path.posix.join("/assets", assetPath).replace(/\\/g, "/");
    return this.ctx.url(normalized);
  });

  return {
    pathPrefix: "/blog/",
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html", "css", "xml", "txt"]
  };
};

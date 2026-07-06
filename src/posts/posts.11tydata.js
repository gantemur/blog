module.exports = {
  eleventyComputed: {
    eleventyExcludeFromCollections: (data) => data.draft === true || data.eleventyExcludeFromCollections,
    permalink: (data) => {
      if (data.draft === true) return false;
      return data.permalink;
    }
  }
};

const fs = require('fs');
const Parser = require('rss-parser');
const parser = new Parser();

(async () => {
    const feed = await parser.parseURL('https://medium.com/feed/@mateusz.w.twardy');
    let markdown = '### 📝 My Latest Medium Articles\n\n';
    feed.items.slice(0, 5).forEach(item => {
        markdown += `- [${item.title}](${item.link})\n`;
    });

    let readme = fs.readFileSync('README.md', 'utf8');
    readme = readme.replace(/<!-- MEDIUM:START -->(.*)<!-- MEDIUM:END -->/s, `<!-- MEDIUM:START -->\n${markdown}\n<!-- MEDIUM:END -->`);
    fs.writeFileSync('README.md', readme, 'utf8');
})();

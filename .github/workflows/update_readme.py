import feedparser
import re

# Replace 'yourusername' with your actual Medium username
RSS_URL = "https://medium.com/feed/@mateusz.w.twardy"

def fetch_medium_articles():
    feed = feedparser.parse(RSS_URL)
    articles = []
    for entry in feed.entries[:5]:  # Fetches the 5 most recent articles
        articles.append({
            "title": entry.title,
            "url": entry.link,
            "published": entry.published_parsed
        })
    return articles

def generate_markdown(articles):
    markdown = "### 📝 My Latest Medium Articles\n\n"
    for article in articles:
        markdown += f"- [{article['title']}]({article['url']})\n"
    return markdown

def update_readme(articles_markdown):
    with open("README.md", "r+") as file:
        content = file.read()
        pattern = r"<!-- MEDIUM:START -->(.*?)<!-- MEDIUM:END -->"
        new_content = re.sub(pattern, f"<!-- MEDIUM:START -->\n{articles_markdown}\n<!-- MEDIUM:END -->", content, flags=re.DOTALL)
        file.seek(0)
        file.write(new_content)
        file.truncate()

if __name__ == "__main__":
    articles = fetch_medium_articles()
    articles_markdown = generate_markdown(articles)
    update_readme(articles_markdown)

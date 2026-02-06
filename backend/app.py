from fastapi import FastAPI
from news_fetcher import fetch_news
from summarizer import summarize_news

app = FastAPI()

@app.get("/news")
def get_news(category: str = "technology"):
    data = fetch_news(category)
    articles = []

    for item in data.get("articles", [])[:5]:
        summary = summarize_news(item.get("content") or item.get("description"))
        articles.append({
            "title": item.get("title"),
            "summary": summary,
            "url": item.get("url")
        })

    return articles

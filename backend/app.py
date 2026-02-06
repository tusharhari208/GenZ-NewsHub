from fastapi import FastAPI
from news_fetcher import fetch_news
from summarizer import summarize_news
from sentiment import analyze_sentiment
from fake_news_checker import check_fake_news

app = FastAPI()

@app.get("/news")
def get_news(category: str = "technology"):
    data = fetch_news(category)
    articles = []

    for item in data.get("articles", [])[:5]:
        content = item.get("content") or item.get("description")

        articles.append({
            "title": item.get("title"),
            "summary": summarize_news(content),
            "sentiment": analyze_sentiment(content),
            "credibility": check_fake_news(content),
            "url": item.get("url")
        })

    return articles

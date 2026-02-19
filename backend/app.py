from fastapi import FastAPI
from backend.news_fetcher import fetch_news
from backend.summarizer import summarize_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GenAI News Aggregator Running"}

@app.get("/news")
def get_news(category: str = "technology"):

    articles = fetch_news(category)

    for article in articles:
        if article["description"]:
            article["summary"] = summarize_text(article["description"])
        else:
            article["summary"] = "No description available."

    return {"articles": articles}

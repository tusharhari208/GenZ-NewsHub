from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.news_fetcher import fetch_news
from backend.summarizer import summarize_text

app = FastAPI()

# ✅ Allow frontend (Vercel) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (safe for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "GenAI News Aggregator Running"}


@app.get("/news")
def get_news(category: str = "technology"):

    articles = fetch_news(category)

    for article in articles:
        if article.get("description"):
            article["summary"] = summarize_text(article["description"])
        else:
            article["summary"] = "No description available."

    return {"articles": articles}

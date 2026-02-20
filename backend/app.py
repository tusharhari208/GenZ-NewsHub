from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.news_fetcher import fetch_news
from backend.summarizer import summarize_text

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for demo
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

    final_articles = []

    for article in articles:
        description = article.get("description")

        if description:
            try:
                article["summary"] = summarize_text(description)
            except:
                article["summary"] = description
        else:
            article["summary"] = "No description available."

        final_articles.append(article)

    return {"articles": final_articles}

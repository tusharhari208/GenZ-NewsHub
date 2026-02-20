import requests
from backend.config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(category="technology"):

    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "country": "us",
        "pageSize": 5,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print("NewsAPI Error:", data)
        return []

    articles = []

    for article in data.get("articles", []):
        articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
        })

    return articles

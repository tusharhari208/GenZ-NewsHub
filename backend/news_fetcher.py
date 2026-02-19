import requests
from backend.config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(category="technology"):
    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "country": "in",
        "pageSize": 5
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    articles = []

    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        })

    return articles

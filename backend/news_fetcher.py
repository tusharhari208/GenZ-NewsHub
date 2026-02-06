import requests

API_KEY = "YOUR_NEWSAPI_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(category):
    params = {
        "apiKey": API_KEY,
        "category": category,
        "language": "en"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

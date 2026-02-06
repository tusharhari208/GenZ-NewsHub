# API Documentation – GenZ NewsHub

## Base URL
http://localhost:8000

---

## GET /news

### Description
Fetches latest news articles and summarizes them using Generative AI.

### Query Parameters
| Parameter | Type   | Description                |
|---------|--------|----------------------------|
| category | string | technology, sports, etc. |

### Example Request
GET /news?category=technology

### Example Response
```json
[
  {
    "title": "AI is transforming healthcare",
    "summary": "- AI improves diagnosis\n- Faster treatments\n- Better patient care",
    "url": "https://news.example.com"
  }
]


---

# 🧠 BACKEND CODE (FastAPI)

### 📁 backend/requirements.txt
```txt
fastapi
uvicorn
requests
openai

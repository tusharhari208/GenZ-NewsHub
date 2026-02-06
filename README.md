# GenZ NewsHub 📰✨

## Project Overview

GenZ NewsHub is an AI-powered News Article Aggregator built for the **HPE GenAI for GenZ Challenge**. The platform collects news articles from multiple trusted sources and uses **Generative AI** to summarize them into short, easy-to-read, GenZ-friendly content.

The goal of this project is to help users stay informed without information overload by providing concise, categorized, and intelligent news summaries.

---

## Problem Statement

Modern users are overwhelmed by long and repetitive news articles spread across multiple platforms. There is a need for a centralized system that:

* Aggregates news from multiple sources
* Uses AI to summarize long articles
* Presents information quickly and clearly

---

## Solution

GenZ NewsHub solves this problem by:

1. Fetching real-time news using public News APIs
2. Processing article content using Generative AI
3. Automatically summarizing and categorizing news
4. Displaying results on a clean and simple web interface

---

## Key Features

* 📰 Multi-source News Aggregation
* 🤖 AI-based News Summarization
* 📂 Category-wise News Filtering
* ⚡ One-Minute News (Quick summaries)
* 😄 GenZ-friendly language output

---

## Creative Feature (Challenge Requirement)

### 🔥 One-Minute News + GenZ Mode

Each news article is summarized into **3 short bullet points**, designed to be readable in under **one minute**, with a casual tone suitable for GenZ users.

---

## Technology Stack

### Frontend

* React.js
* HTML, CSS, JavaScript

### Backend

* Python
* FastAPI

### Generative AI

* OpenAI API / HuggingFace API

### News Source

* NewsAPI.org / RSS Feeds

---

## System Architecture

1. User selects a news category from the frontend
2. Frontend sends request to backend API
3. Backend fetches news from NewsAPI
4. Article content is sent to GenAI for summarization
5. Summarized news is returned to frontend

---

## Folder Structure

```
genz-newshub/
│
├── backend/
│   ├── app.py
│   ├── news_fetcher.py
│   ├── summarizer.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│
├── docs/
│   ├── architecture.md
│   ├── api-docs.md
│
├── README.md
└── .gitignore
```

---

## Installation & Setup

### Backend Setup

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

### Frontend Setup

```bash
npm install
npm start
```

---

## API Endpoints

### Get News

```
GET /news?category=technology
```

**Response:**

* Title
* AI-generated summary
* Article URL

---

## Future Enhancements

* Fake news detection using AI
* Voice-based news summaries
* Regional language support
* Personalized news recommendations

---

## Build in Public

The development journey of this project is shared on LinkedIn as part of the challenge requirement.

---

## Conclusion

GenZ NewsHub demonstrates the practical use of Generative AI in solving real-world problems by making news consumption faster, smarter, and more engaging for GenZ users.

---

## Author

**Tushar Hari**

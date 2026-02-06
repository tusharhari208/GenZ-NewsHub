# GenZ NewsHub 📰✨

## Project Overview

GenZ NewsHub is an **AI-powered News Article Aggregator** developed for the **HPE GenAI for GenZ Challenge**. The platform aggregates news from multiple trusted sources and uses **Generative AI** to summarize articles, analyze sentiment, and provide AI-assisted credibility insights.

The project focuses on making news consumption **fast, simple, and responsible**, especially for GenZ users.

---

## Problem Statement

Today’s news ecosystem suffers from:

* Information overload
* Long and repetitive articles
* Difficulty in identifying biased or misleading news

Users need a centralized platform that not only aggregates news but also **intelligently processes it using AI**.

---

## Proposed Solution

GenZ NewsHub solves these problems by:

1. Aggregating news from multiple sources using APIs
2. Using Generative AI to summarize long articles
3. Performing sentiment analysis on news content
4. Providing AI-assisted fake news / credibility detection
5. Presenting everything in a clean GenZ-friendly UI

---

## Key Features

* 📰 Multi-source News Aggregation
* 🤖 AI-based News Summarization (One‑Minute News)
* 😄 GenZ-friendly bullet-point summaries
* 😊 Sentiment Analysis (Positive / Neutral / Negative)
* 🛡️ AI-assisted Fake News / Credibility Detection
* 📂 Category-wise News Filtering

---

## Creative Features (Challenge Requirement)

### 🔥 Responsible News AI

Unlike basic aggregators, GenZ NewsHub adds **AI-powered sentiment and credibility insights**, helping users:

* Understand emotional tone of news
* Be aware of potentially misleading content

⚠️ *Note:* Credibility detection is AI-assisted and does not replace professional fact-checking.

---

## Technology Stack

### Frontend

* React.js
* HTML, CSS, JavaScript

### Backend

* Python
* FastAPI

### Generative AI

* OpenAI API (Summarization, Sentiment Analysis, Credibility Estimation)

### News Data Source

* NewsAPI.org / RSS Feeds

---

## System Architecture

1. User selects a news category from the frontend
2. Frontend sends request to backend API
3. Backend fetches news from NewsAPI
4. Article content is processed by GenAI modules:

   * Summarization
   * Sentiment Analysis
   * Credibility Check
5. Processed news is returned to frontend
6. Frontend displays summarized news with AI insights

---

## Folder Structure

```
genz-newshub/
│
├── backend/
│   ├── app.py
│   ├── news_fetcher.py
│   ├── summarizer.py
│   ├── sentiment.py
│   ├── fake_news_checker.py
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

## API Overview

### Endpoint

```
GET /news?category=technology
```

### Returns

* News title
* AI-generated summary
* Sentiment label
* Credibility estimation
* Article URL

---

## Future Enhancements

* Personalized news recommendations
* Regional language support
* Voice-based news summaries
* Advanced misinformation detection models

---

## Conclusion

GenZ NewsHub demonstrates how Generative AI can be used responsibly to improve information consumption by combining **summarization, sentiment analysis, and credibility awareness** into a single platform.

---

## Author

**Tushar Hari**

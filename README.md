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


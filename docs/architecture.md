# System Architecture – GenZ NewsHub

## Architecture Overview
GenZ NewsHub uses a client-server architecture enhanced with Generative AI services.

## Main Components
1. Frontend – React.js
2. Backend – FastAPI (Python)
3. News Data Source – NewsAPI / RSS Feeds
4. GenAI Engine – OpenAI API

## Functional Modules
- News Aggregation Module
- AI Summarization Module
- Sentiment Analysis Module
- Fake News / Credibility Detection Module

## Architecture Flow
1. User selects a news category
2. Frontend sends API request to backend
3. Backend fetches raw news articles
4. Each article is processed by GenAI:
   - Summarized into short bullet points
   - Sentiment analyzed (Positive / Neutral / Negative)
   - Credibility estimated (Likely Genuine / Possibly Misleading / Unverified)
5. Processed data is returned to frontend
6. Frontend displays AI-enhanced news cards

## Architecture Diagram (Textual)
User  
 ↓  
Frontend (React)  
 ↓  
Backend (FastAPI)  
 ↓  
News API → GenAI Engine  
 ↓  
Summarized + Analyzed News  
 ↓  
Frontend UI

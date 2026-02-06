# System Architecture – GenZ NewsHub

## Overview
GenZ NewsHub follows a client-server architecture with Generative AI integration.

## Components
1. Frontend (React.js)
2. Backend (FastAPI – Python)
3. News Data Source (NewsAPI / RSS)
4. GenAI Engine (OpenAI / HuggingFace)

## Architecture Flow
1. User selects a news category from the UI
2. Frontend sends request to backend API
3. Backend fetches news articles from NewsAPI
4. Each article content is sent to GenAI for summarization
5. AI-generated summary is returned to frontend
6. Frontend displays summarized news cards

## Advantages
- Modular design
- Scalable backend
- Easy GenAI integration
- Clean separation of concerns

## Diagram (Textual)
User → Frontend → Backend → News API  
                       ↳ GenAI → Summary → Frontend

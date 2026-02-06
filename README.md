# Market-sentiment-analysis
A Real-Time Retrieval-Augmented Generation (RAG) tool that fetches the latest financial news and uses Llama 3 (via Ollama) to generate deep-dive market sentiment reports.
Features
- Real-Time Data: Pulls the top 25 headlines from Alpha Vantage's Market News & Sentiment API.
- Topic-Based Analysis: Filters news across Technology, IPOs, Blockchain, and Finance.
- Local LLM Reasoning: Processes data locally using Llama 3 for maximum privacy and no per-token costs.
- Zero Hallucination:Uses a strictly grounded RAG prompt to ensure the AI only reports on actual news provided.
# Tech Stack
- Language:Python 
- LLM Framework:LangChain / LangChain-Groq
- Model: llama-3.3-70b-versatile
- Data Source: Alpha Vantage API
# Setup
Install dependencies
- pip install langchain langchain-groq
- Configure Environment Variables
- Create a .env file in the root directory and add your Alpha Vantage API Key & Groq API Key:


# Future Roadmap: Scaling with TensorFlow
The next phase of this project involves:

Historical Data Logging: Saving sentiment scores into a CSV/SQL database.

Predictive Modeling: Training a TensorFlow LSTM model to correlate news sentiment trends with historical price movements.

Feature Engineering: Using Natural Language Processing (NLP) to weight sentiment by "relevance" scores.

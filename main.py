
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_key = os.getenv("API_key")


def news_sentiment():
    """
    to fetch the latest news sentiment and headlines 
    """
    try:
        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=technology,ipo,blockchain,finance,mergers_and_acquisitions&limit=25&apikey={API_key}'
        r = requests.get(url)
        data = r.json()
        if "Information" in data or "Note" in data:
            return f"API LIMIT REACHED: {data.get('Information') or data.get('Note')}"
        feed = data.get("feed", [])
        report = []
        for articles in feed:
            title = articles.get("title")
            sentiment = articles.get("overall_sentiment_label")
            report.append(f"[{sentiment}]{title}")

        return "\n".join(report)
    except Exception as e:
        return f"Error connecting to Alpha Vantage: {e}"




llm=ChatOllama(model="llama3",temperature=.1)

def gen_report():
    news_data=news_sentiment()
    model=ChatOllama(model="llama3",temperature=.1 )
    prompt= f"""You are a professional market analyst. Here are the latest 25 headlines:
    
    {news_data}
    
    TASK:
    1. List all 25 headlines with their sentiment.
    2. Identify the 3 biggest trends currently driving these markets.
    3. Based on these specific 25 articles, what is the overall market mood?
    
    IMPORTANT: Do not summarize or skip headlines. List them all.
    """ 
    response=model.invoke(prompt)
    print(response.content)


gen_report ()
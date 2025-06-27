import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def news_agent(query, page_size=3):
    if not NEWS_API_KEY:
        print("❌ Error: NEWS_API_KEY is not set in .env")
        return []

    print(f"📰 Fetching news for: {query}")

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&"
        f"pageSize={page_size}&"
        f"sortBy=publishedAt&"
        f"apiKey={NEWS_API_KEY}"
    )
    
    response = requests.get(url)
    print(f"🔁 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [{"title": art["title"], "url": art["url"]} for art in articles]
    else:
        print(f"❌ News API error: {response.status_code} - {response.text}")
        return []

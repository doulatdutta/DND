# ipo/news_researcher.py

import requests
import pandas as pd

class IPO_NewsResearcher:
    def __init__(self):
        self.news_data = []

    def collect_ipo_news(self):
        # Example API endpoint for gathering IPO news (change to actual API)
        url = "https://newsapi.org/v2/everything?q=IPO&apiKey=YOUR_API_KEY"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            self.news_data = [
                {
                    "title": article["title"],
                    "description": article["description"],
                    "url": article["url"],
                    "publishedAt": article["publishedAt"]
                }
                for article in articles
            ]
        else:
            print(f"Failed to retrieve IPO news: {response.status_code}")

    def get_news_data(self):
        return pd.DataFrame(self.news_data)

if __name__ == "__main__":
    researcher = IPO_NewsResearcher()
    researcher.collect_ipo_news()
    news_df = researcher.get_news_data()
    print(news_df)

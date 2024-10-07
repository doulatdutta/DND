# select_sector/news_researcher.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

class SectorNewsResearcher:
    def __init__(self, sector):
        self.sector = sector
        self.news_data = []

    def collect_news(self):
        # Placeholder for the news source URL
        url = f"https://newsapi.org/v2/everything?q={self.sector}&apiKey=YOUR_API_KEY"
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
            print(f"Failed to retrieve news: {response.status_code}")

    def get_news_data(self):
        return pd.DataFrame(self.news_data)

if __name__ == "__main__":
    sector = input("Enter sector to research: ")
    researcher = SectorNewsResearcher(sector)
    researcher.collect_news()
    news_df = researcher.get_news_data()
    print(news_df)

# overall_next_day/news_researcher.py

import requests
import pandas as pd

class OverallNewsResearcher:
    def __init__(self):
        self.news_data = []

    def collect_top_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"
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
    researcher = OverallNewsResearcher()
    researcher.collect_top_news()
    news_df = researcher.get_news_data()
    print(news_df)

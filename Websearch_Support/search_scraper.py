import requests
from bs4 import BeautifulSoup

class SearchScraper:
    def __init__(self):
        self.search_url = "https://www.google.com/search?q="

    def scrape_results(self, query):
        """
        Scrapes search results from Google.
        """
        try:
            response = requests.get(self.search_url + query)
            soup = BeautifulSoup(response.text, 'html.parser')

            results = []
            for item in soup.find_all('h3'):
                results.append(item.get_text())
            
            print(f"Scraped results for '{query}':")
            for result in results[:5]:  # Show top 5 results
                print(result)
                
            return results[:5]  # Return top 5 results
        except Exception as e:
            print(f"Scraping failed: {e}")
            return None

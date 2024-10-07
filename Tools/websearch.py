import requests
from bs4 import BeautifulSoup

class WebSearch:
    def __init__(self):
        self.search_url = "https://www.google.com/search?q="

    def search(self, query):
        """
        Searches the web for the provided query and returns top results.
        """
        try:
            search_response = requests.get(self.search_url + query)
            soup = BeautifulSoup(search_response.text, 'html.parser')
            
            # Extracting top results (this is basic scraping; adapt as needed)
            results = []
            for item in soup.find_all('h3'):
                results.append(item.get_text())
            
            print(f"Search results for '{query}':")
            for result in results[:5]:  # Show top 5 results
                print(result)
                
            return results[:5]  # Returning top 5 results
        except Exception as e:
            print(f"Web search failed: {e}")
            return None

    def get_tutorial(self, topic):
        """
        Searches for tutorials or articles on a specific topic.
        """
        query = f"{topic} tutorial"
        return self.search(query)

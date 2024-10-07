from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class ChromeTool:
    def __init__(self, driver_path="D:\\buisness\\AI\\DND\\chromedriver-win64\\chromedriver.exe"):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for automation
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def open_page(self, url):
        """
        Opens a webpage using Google Chrome.
        """
        self.driver.get(url)
        print(f"Opened page: {url}")
        time.sleep(2)  # Allow the page to load

    def scrape_text_by_selector(self, selector):
        """
        Scrapes text content from the webpage by a given CSS selector.
        """
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            return element.text
        except Exception as e:
            print(f"Failed to scrape text: {e}")
            return None

    def close_browser(self):
        """
        Closes the Chrome browser.
        """
        self.driver.quit()
        print("Chrome browser closed.")

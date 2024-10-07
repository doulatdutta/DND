import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.database_url = os.getenv("DATABASE_URL")

    def display_config(self):
        """
        Displays the current configuration settings.
        """
        print("Current Configuration Settings:")
        print(f"OpenAI API Key: {self.openai_api_key}")
        print(f"Google API Key: {self.google_api_key}")
        print(f"Database URL: {self.database_url}")

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")
API_URL = os.getenv("API_URL", "https://demoqa.com")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_password(key):
    return os.getenv(key)
# (c)TechRewindEditz

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
class Config:
    USER_AGENT = "(Google Chrome Android/131.0.6778.200; ios/131.0.6778.154) (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    TIMEOUT = 30
    MAX_RETRIES = 3
    CHUNK_SIZE = 8192
    DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "downloads")
    
    # Create download directory if it doesn't exist
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)


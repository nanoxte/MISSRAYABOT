import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot Information
    BOT_NAME = "MISSRAYABOT"
    VERSION = "1.0.0"
    AUTHOR = "TechRewindEditz"
    LAST_UPDATED = "2024-12-25"

    # Streaming Configuration
    STREAM_QUALITY = {
        "4K": "2160p",
        "FHD": "1080p",
        "HD": "720p",
        "SD": "480p"
    }
    
    DEFAULT_QUALITY = "HD"
    BUFFER_SIZE = 8192 * 1024  # 8MB Buffer
    
    # MXPlayer Configuration
    MXPLAYER_PATH = os.getenv("MXPLAYER_PATH", "mxplayer")
    PLAYER_ARGS = ["--fullscreen", "--audio-delay=0"]
    
    # Supported Sites
    SUPPORTED_SITES = [
        "https://movies4u.bz",
        "https://www.azmovies.net",
        "https://www.fzmovies.ng",
        "https://www.terabox.com",
        "https://shareus.io",
        # Add more supported sites
    ]
    
    # File Types
    SUPPORTED_FORMATS = [
        ".mp4", ".mkv", ".avi", ".mov",
        ".m3u8", ".m3u", ".mpd"
    ]
    
    # Database
    DB_URL = os.getenv("DATABASE_URL", "mongodb+srv://theaashsaifi:ZalWHlfqRt4xCjFH@rayaofficial.vz5rs.mongodb.net/?retryWrites=true&w=majority&appName=RAYAOFFICIAL")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = "logs/stream.log"
    
    @classmethod
    def is_supported_site(cls, url):
        return any(site in url for site in cls.SUPPORTED_SITES)
    
    @classmethod
    def is_supported_format(cls, url):
        return any(fmt in url.lower() for fmt in cls.SUPPORTED_FORMATS)

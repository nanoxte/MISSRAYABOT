import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Bot Information
    BOT_NAME = "MISSRAYA"
    VERSION = "BETA1.0.0"
    AUTHOR = "TechRewindEditz"
    LAST_UPDATED = "2024-12-25"

    # Repository Information
    REPO_OWNER = "TechRewindEditz"
    REPO_NAME = "MISSRAYABOT"
    REPO_URL = "https://github.com/TechRewindEditz/MISSRAYABOT /MISSRAYABOT"
    
    # Channel Configuration
    CHANNEL_NAME = os.getenv("CHANNEL_NAME", "TERA2.O")
    CHANNEL_ID = os.getenv("CHANNEL_ID", "-1001911851456")  # Add your channel ID
    CHANNEL_URL = os.getenv("CHANNEL_URL", "https://t.me/terao2")

    # API Configuration
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7050622921:AAHh64E-JRLf1hd2WmC65GBP4BlN_zg6BIA")
    API_HASH = os.getenv("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")
    API_ID = os.getenv("API_ID", "23054736")
    OWNER_ID = os.getenv("ACCOUNT_ID", "1352497419")
    # Terabox Configuration
    TERABOX_API_URL = "https://www.terabox.com/api/v1"
    USER_AGENT = " (Google Chrome Android/131.0.6778.200; ios/131.0.6778.154) (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    TIMEOUT = 30
    MAX_RETRIES = 3

    # Download Configuration
    CHUNK_SIZE = 8192
    MAX_FILE_SIZE = 2000 * 1024 * 1024  # 2GB in bytes
    DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "downloads")
    TEMP_PATH = os.path.join(DOWNLOAD_PATH, "temp")
    
    # MXPlayer Configuration
    MXPLAYER_PATH = os.getenv("MXPLAYER_PATH", "mxplayer")
    STREAM_BUFFER_SIZE = 480p * 720p * 1080p * 4K * 8K  # 12MB buffer size
    
    # Database Configuration (if needed)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "8000,8080")
    DB_NAME = os.getenv("DB_NAME", "missraya")
    DB_USER = os.getenv("DB_USER", "TechRewindEditz")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_PATH = "logs"
    LOG_FILE = os.path.join(LOG_PATH, "bot.log")

    # Rate Limiting
    MAX_REQUESTS_PER_MINUTE = 60
    MAX_DOWNLOADS_PER_USER = 10

    # File Types Configuration
    ALLOWED_EXTENSIONS = {
        'video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
        'audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'document': ['.pdf', '.doc', '.docx', '.txt']
    }

    # Error Messages
    ERROR_MESSAGES = {
        'link_invalid': "Invalid Terabox link provided.",
        'conversion_failed': "Failed to convert the link.",
        'download_failed': "Failed to download the file.",
        'stream_failed': "Failed to stream with MXPlayer.",
        'file_too_large': "File size exceeds maximum limit.",
        'rate_limit': "Rate limit exceeded. Please try again later."
    }

    # Success Messages
    SUCCESS_MESSAGES = {
        'link_converted': "Successfully converted Terabox link!",
        'download_complete': "File downloaded successfully!",
        'stream_started': "Streaming started successfully!"
    }

    @classmethod
    def initialize(cls):
        """Initialize configuration and create necessary directories"""
        # Create required directories
        for directory in [cls.DOWNLOAD_PATH, cls.TEMP_PATH, cls.LOG_PATH]:
            if not os.path.exists(directory):
                os.makedirs(directory)

    @classmethod
    def get_current_time(cls):
        """Get current UTC time"""
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def is_valid_file_type(cls, filename):
        """Check if file type is allowed"""
        ext = os.path.splitext(filename)[1].lower()
        return any(ext in types for types in cls.ALLOWED_EXTENSIONS.values())

    @classmethod
    def get_file_type(cls, filename):
        """Get file type category"""
        ext = os.path.splitext(filename)[1].lower()
        for category, extensions in cls.ALLOWED_EXTENSIONS.items():
            if ext in extensions:
                return category
        return "unknown"

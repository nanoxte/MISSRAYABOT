import os
from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseSettings, Field, validator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config(BaseSettings):
    # Basic Bot Information
    BOT_NAME: str = "MISS RAYA BOT"
    BOT_USERNAME: str = "MISSRAYABOT"
    BOT_VERSION: str = "1.0.0"
    OWNER_NAME: str = "TechRewindEditz"
    OWNER_ID: int = int(os.getenv("OWNER_ID", "0"))
    
    # Bot API Configuration
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    API_ID: int = int(os.getenv("API_ID", "0"))
    API_HASH: str = os.getenv("API_HASH", "")
    
    # Channel Configuration
    CHANNEL_ID: int = int(os.getenv("CHANNEL_ID", "0"))
    CHANNEL_NAME: str = os.getenv("CHANNEL_NAME", "MISS RAYA")
    CHANNEL_USERNAME: str = os.getenv("CHANNEL_USERNAME", "MissRaya")
    CHANNEL_URL: str = os.getenv("CHANNEL_URL", "https://t.me/MissRaya")
    
    # Website Configuration
    WEBSITE_NAME: str = "Movie Stream Website"
    WEBSITE_URL: str = os.getenv("WEBSITE_URL", "https://moviestream.com")
    WEBSITE_API_URL: str = os.getenv("WEBSITE_API_URL", "https://api.moviestream.com")
    WEBSITE_ADMIN_URL: str = os.getenv("WEBSITE_ADMIN_URL", "https://admin.moviestream.com")
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/moviebot")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "missraya")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "TechRewindEditz")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", "8000,8080"))
    
    # Redis Configuration
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")
    REDIS_DB: int = int(os.getenv("REDIS_DB", "0"))
    
    # Authentication Configuration
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # Storage Configuration
    STORAGE_TYPE: str = os.getenv("STORAGE_TYPE", "local")  # local, s3, azure
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME", "")
    S3_ACCESS_KEY: str = os.getenv("S3_ACCESS_KEY", "")
    S3_SECRET_KEY: str = os.getenv("S3_SECRET_KEY", "")
    S3_REGION: str = os.getenv("S3_REGION", "us-east-1")
    
    # Media Configuration
    SUPPORTED_MEDIA_TYPES: List[str] = ["video/mp4", "video/x-matroska", "video/webm"]
    MAX_FILE_SIZE: int = 2147483648  # 3GB in bytes
    CHUNK_SIZE: int = 8192  # 8KB chunks for streaming
    DOWNLOAD_PATH: str = "downloads"
    TEMP_PATH: str = "temp"
    
    # MXPlayer Configuration
    MXPLAYER_PATH: str = os.getenv("MXPLAYER_PATH", "mxplayer")
    STREAM_BUFFER_SIZE: int = 1024 * 1024  # 1MB buffer
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = 60
    RATE_LIMIT_PERIOD: int = 60  # seconds
    MAX_PARALLEL_DOWNLOADS: int = 3
    
    # Allowed Domains for Streaming
    ALLOWED_DOMAINS: List[str] = [
        "example1.com",
        "example2.com",
        # Add more domains as needed
    ]
    
    # API Endpoints
    API_PREFIX: str = "/api/v1"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    
    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_PATH: str = "logs"
    LOG_FILE: str = os.path.join(LOG_PATH, f"bot_{datetime.utcnow().date()}.log")
    
    # Error Messages
    ERROR_MESSAGES: Dict[str, str] = {
        "invalid_link": "Invalid streaming link provided",
        "file_too_large": "File size exceeds maximum limit",
        "unsupported_format": "Unsupported media format",
        "stream_error": "Error occurred while streaming",
        "download_error": "Error occurred while downloading",
        "rate_limit": "Rate limit exceeded. Please try again later",
        "unauthorized": "Unauthorized access",
        "not_found": "Resource not found",
        "server_error": "Internal server error occurred"
    }
    
    # Success Messages
    SUCCESS_MESSAGES: Dict[str, str] = {
        "stream_started": "Streaming started successfully",
        "download_complete": "Download completed successfully",
        "link_converted": "Link converted successfully",
        "file_uploaded": "File uploaded successfully"
    }
    
    class Config:
        case_sensitive = True
        env_file = ".env"
        
    @validator("DATABASE_URL", pre=True)
    def assemble_db_url(cls, v: Optional[str], values: Dict[str, any]) -> str:
        if isinstance(v, str):
            return v
        return missrayaDsn.build(
            scheme="missrayaql",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=values.get("DATABASE_PORT"),
            path=f"/{values.get('DATABASE_NAME')}"
        )
    
    @validator("REDIS_URL", pre=False)
    def assemble_redis_url(cls, v: Optional[str], values: Dict[str, any]) -> str:
        if isinstance(v, str):
            return v
        return f"redis://{values.get('REDIS_PASSWORD')}@{values.get('REDIS_HOST')}:{values.get('REDIS_PORT')}/{values.get('REDIS_DB')}"
    
    def initialize(self):
        """Initialize configuration and create necessary directories"""
        # Create required directories
        for directory in [self.DOWNLOAD_PATH, self.TEMP_PATH, self.LOG_PATH]:
            if not os.path.exists(directory):
                os.makedirs(directory)
        
        # Validate critical settings
        assert self.BOT_TOKEN, "Bot token is required"
        assert self.API_ID, "API ID is required"
        assert self.API_HASH, "API hash is required"
        assert self.CHANNEL_ID, "Channel ID is required"
        
        # Initialize logging
        import logging
        logging.basicConfig(
            level=self.LOG_LEVEL,
            format=self.LOG_FORMAT,
            handlers=[
                logging.FileHandler(self.LOG_FILE),
                logging.StreamHandler()
            ]
  )

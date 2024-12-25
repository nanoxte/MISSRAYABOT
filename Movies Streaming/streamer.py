import subprocess
from .config import Config
from .utils.logger import setup_logger

logger = setup_logger(__name__)

class StreamManager:
    def __init__(self):
        self.current_process = None
        
    def start_stream(self, url, quality=Config.DEFAULT_QUALITY):
        """Start streaming using MXPlayer"""
        try:
            command = [
                Config.MXPLAYER_PATH,
                url,
                *Config.PLAYER_ARGS
            ]
            
            if quality in Config.STREAM_QUALITY:
                command.append(f"--quality={Config.STREAM_QUALITY[quality]}")
            
            self.current_process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            logger.info(f"Started streaming: {url}")
            return True
            
        except Exception as e:
            logger.error(f"Streaming error: {str(e)}")
            return False
    
    def stop_stream(self):
        """Stop current stream"""
        if self.current_process:
            self.current_process.terminate()
            self.current_process = None
            logger.info("Stream stopped")

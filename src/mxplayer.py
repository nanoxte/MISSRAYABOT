import subprocess
from .utils import logger

class MXPlayer:
    @staticmethod
    def stream(direct_link):
        """Stream media using MXPlayer."""
        try:
            # Attempt to start MXPlayer with the direct link
            process = subprocess.Popen(
                ['mxplayer', direct_link],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Wait for the process to complete
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                logger.error(f"MXPlayer error: {stderr.decode()}")
                return False
                
            return True
        except Exception as e:
            logger.error(f"Error streaming with MXPlayer: {str(e)}")
            return False

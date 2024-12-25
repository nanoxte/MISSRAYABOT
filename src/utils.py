import logging
from colorama import init, Fore
from tqdm import tqdm
import requests
from pathlib import Path
from .config import Config

# Initialize colorama
init()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def download_file(url, filename):
    """Download file with progress bar."""
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        # Create the downloads directory if it doesn't exist
        download_path = Path(Config.DOWNLOAD_PATH)
        download_path.mkdir(parents=True, exist_ok=True)
        
        file_path = download_path / filename
        
        with open(file_path, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=Config.CHUNK_SIZE):
                size = file.write(data)
                pbar.update(size)
                
        return True
    except Exception as e:
        logger.error(f"Error downloading file: {str(e)}")
        return False

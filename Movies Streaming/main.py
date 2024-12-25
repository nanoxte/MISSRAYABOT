import sys
from .streamer import StreamManager
from .converter import LinkConverter
from .database import Database
from .config import Config
from .utils.logger import setup_logger
from colorama import init, Fore, Style

init()  # Initialize colorama
logger = setup_logger(__name__)

class MovieStreamBot:
    def __init__(self):
        self.streamer = StreamManager()
        self.converter = LinkConverter()
        self.db = Database()
        
    def start(self):
        print(f"{Fore.CYAN}{Config.BOT_NAME} v{Config.VERSION}{Style.RESET_ALL}")
        print("=" * 50)
        
        while True:
            try:
                url = input(f"\n{Fore.GREEN}Enter movie URL (or 'q' to quit): {Style.RESET_ALL}")
                
                if url.lower() == 'q':
                    break
                    
                if not Config.is_supported_site(url):
                    print(f"{Fore.RED}Unsupported website!{Style.RESET_ALL}")
                    continue
                
                print(f"{Fore.YELLOW}Converting link...{Style.RESET_ALL}")
                stream_url = self.converter.extract_stream_url(url)
                
                if not stream_url:
                    print(f"{Fore.RED}Failed to extract stream URL!{Style.RESET_ALL}")
                    continue
                
                print("\nAvailable qualities:")
                for i, quality in enumerate(Config.STREAM_QUALITY.keys(), 1):
                    print(f"{i}. {quality}")
                
                quality_choice = input(f"\n{Fore.GREEN}Select quality (1-{len(Config.STREAM_QUALITY)}): {Style.RESET_ALL}")
                quality = list(Config.STREAM_QUALITY.keys())[int(quality_choice) - 1]
                
                print(f"\n{Fore.YELLOW}Starting stream...{Style.RESET_ALL}")
                if self.streamer.start_stream(stream_url, quality):
                    print(f"{Fore.GREEN}Streaming started successfully!{Style.RESET_ALL}")
                    self.db.add_stream("Movie", url, quality)
                else:
                    print(f"{Fore.RED}Failed to start streaming!{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Stopping stream...{Style.RESET_ALL}")
                self.streamer.stop_stream()
                break
                
            except Exception as e:
                logger.error(f"Error: {str(e)}")
                print(f"{Fore.RED}An error occurred! Check logs for details.{Style.RESET_ALL}")

def main():
    bot = MovieStreamBot()
    bot.start()

if __name__ == "__main__":
    main()

from converter import TeraboxConverter
from mxplayer import MXPlayer
from utils import download_file, logger
from colorama import Fore, Style

def main():
    print(f"{Fore.CYAN}Terabox Link Converter Bot{Style.RESET_ALL}")
    print("=" * 40)
    
    while True:
        terabox_link = input(f"\n{Fore.GREEN}Enter Terabox link (or 'q' to quit): {Style.RESET_ALL}")
        
        if terabox_link.lower() == 'q':
            break
            
        converter = TeraboxConverter()
        direct_link = converter.convert_link(terabox_link)
        
        if direct_link:
            print(f"\n{Fore.BLUE}Direct download link:{Style.RESET_ALL} {direct_link}")
            
            choice = input(f"\n{Fore.YELLOW}Choose an option:\n"
                         "1. Stream with MXPlayer\n"
                         "2. Download file\n"
                         "3. Copy link only\n"
                         "Choice (1-3): {Style.RESET_ALL}")
            
            if choice == '1':
                print("\nStreaming with MXPlayer...")
                if MXPlayer.stream(direct_link):
                    print(f"{Fore.GREEN}Streaming started successfully!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Failed to start streaming.{Style.RESET_ALL}")
                    
            elif choice == '2':
                filename = input(f"\n{Fore.YELLOW}Enter filename to save as: {Style.RESET_ALL}")
                print("\nDownloading file...")
                if download_file(direct_link, filename):
                    print(f"{Fore.GREEN}Download completed successfully!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Download failed.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to convert link. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Bot stopped by user.{Style.RESET_ALL}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        print(f"{Fore.RED}An unexpected error occurred. Please check the logs.{Style.RESET_ALL}")

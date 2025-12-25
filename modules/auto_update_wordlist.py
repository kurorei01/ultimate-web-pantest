import requests
import logging
import os

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def auto_update_wordlist(url: str, file_path: str) -> bool:
    """
    Download and append wordlist from a URL to a local file.
    
    Args:
        url: URL to download the wordlist from
        file_path: Local file path to append the wordlist to
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Download the wordlist with timeout
        logging.info(f"Downloading wordlist from {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Validate that we got some content
        if not response.text.strip():
            logging.warning(f"Empty wordlist received from {url}")
            print(f"[!] Warning: Empty wordlist from {url}")
            return False
        
        # Append to file
        with open(file_path, "a", encoding="utf-8") as f:
            # Add newline if file doesn't end with one
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                f.write("\n")
            f.write(response.text)
        
        logging.info(f"Wordlist successfully updated: {file_path}")
        print(f"[+] Wordlist updated: {file_path}")
        return True
        
    except requests.exceptions.Timeout:
        logging.error(f"Timeout while downloading wordlist from {url}")
        print(f"[!] Timeout: Could not download from {url}")
        return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error while downloading wordlist: {e}")
        print(f"[!] Request Error: {e}")
        return False
    except IOError as e:
        logging.error(f"File error while writing wordlist: {e}")
        print(f"[!] File Error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during wordlist update: {e}")
        print(f"[!] Unexpected Error: {e}")
        return False
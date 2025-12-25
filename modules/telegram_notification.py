import requests
import logging
import os

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_telegram_notification(message: str, bot_token: str, chat_id: str) -> bool:
    """
    Send a notification via Telegram bot.
    
    Args:
        message: Message to send
        bot_token: Telegram bot API token
        chat_id: Telegram chat ID to send message to
        
    Returns:
        bool: True if message sent successfully, False otherwise
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    
    try:
        logging.info(f"Sending Telegram notification to chat_id: {chat_id}")
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        
        if response.json().get("ok"):
            logging.info("Telegram notification sent successfully")
            print(f"[+] Notifikasi Telegram terkirim")
            return True
        else:
            logging.warning("Telegram notification failed")
            print(f"[-] Notifikasi Telegram gagal")
            return False
            
    except requests.exceptions.Timeout:
        logging.error("Timeout while sending Telegram notification")
        print(f"[!] Timeout: Telegram API")
        return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error while sending Telegram notification: {e}")
        print(f"[!] Request Error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error while sending Telegram notification: {e}")
        print(f"[!] Unexpected Error: {e}")
        return False
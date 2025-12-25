import logging
import os

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_result(username: str, password: str, status: str) -> None:
    logging.info(f"{username}:{password} - {status}")


import random
from typing import Dict, List

def get_proxy() -> Dict[str, str]:
    """
    Get a random proxy from the proxy pool.
    
    Returns:
        dict: Proxy configuration dictionary with 'http' and optionally 'https' keys
    """
    proxies: List[Dict[str, str]] = [
        {"http": "http://proxy1:port", "https": "http://proxy1:port"},
        {"http": "http://proxy2:port", "https": "http://proxy2:port"}
    ]
    return random.choice(proxies)
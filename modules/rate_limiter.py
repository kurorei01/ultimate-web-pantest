import time
import random

def delay_request(min_delay: float = 1, max_delay: float = 3) -> None:
    time.sleep(random.uniform(min_delay, max_delay))
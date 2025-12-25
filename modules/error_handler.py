import time
from typing import Callable, TypeVar

T = TypeVar('T')

def retry_on_error(func: Callable[[], T], retries: int = 3, delay: int = 2) -> T:
    """
    Retry a function on error with exponential backoff.
    
    Args:
        func: Function to retry
        retries: Number of retry attempts
        delay: Delay in seconds between retries
        
    Returns:
        The return value of the function
        
    Raises:
        Exception: The last exception if all retries fail
    """
    last_exception: Exception = Exception("No attempts made")
    
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            if i < retries - 1:
                time.sleep(delay)
    
    raise last_exception
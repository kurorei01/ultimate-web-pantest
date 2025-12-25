from typing import List

def read_wordlist(file_path: str) -> List[str]:
    """
    Read a wordlist file and return a list of words.
    
    Args:
        file_path: Path to the wordlist file
        
    Returns:
        list: List of words from the file (stripped of whitespace)
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]
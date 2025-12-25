import os
from typing import Dict, Any, Optional, List

class Config:
    """Configuration manager for automated penetration testing"""
    
    def __init__(self) -> None:
        # Target Configuration
        self.target_url: str = os.environ.get('TARGET_URL', 'http://target.com')
        self.target_login_url: str = os.environ.get('TARGET_LOGIN_URL', f'{self.target_url}/login.php')
        self.target_search_url: str = os.environ.get('TARGET_SEARCH_URL', f'{self.target_url}/search.php')
        self.target_contact_url: str = os.environ.get('TARGET_CONTACT_URL', f'{self.target_url}/contact.php')
        self.target_admin_url: str = os.environ.get('TARGET_ADMIN_URL', f'{self.target_url}/admin')
        self.target_mfa_url: str = os.environ.get('TARGET_MFA_URL', f'{self.target_url}/mfa')
        
        # Credentials
        self.username: str = os.environ.get('DEFAULT_USERNAME', 'admin')
        self.wordlist_path: str = os.environ.get('WORDLIST_PATH', 'wordlists/passwords.txt')
        
        # API Keys
        self.captcha_api_key: str = os.environ.get('CAPTCHA_API_KEY', '')
        self.captcha_url: str = os.environ.get('CAPTCHA_URL', '')
        
        # Telegram Configuration
        self.telegram_bot_token: str = os.environ.get('TELEGRAM_BOT_TOKEN', '')
        self.telegram_chat_id: str = os.environ.get('TELEGRAM_CHAT_ID', '')
        
        # Wordlist Update
        self.wordlist_update_url: str = os.environ.get('WORDLIST_UPDATE_URL', 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt')
        
        # Testing Parameters
        self.test_param: str = os.environ.get('TEST_PARAM', 'q')
        self.sql_param: str = os.environ.get('SQL_PARAM', 'id')
        self.xss_param: str = os.environ.get('XSS_PARAM', 'message')
        
        # Encryption
        self.encryption_key: Optional[str] = os.environ.get('ENCRYPTION_KEY', None)
        
        # Feature Flags
        self.enable_bruteforce: bool = os.environ.get('ENABLE_BRUTEFORCE', 'true').lower() == 'true'
        self.enable_sql_injection: bool = os.environ.get('ENABLE_SQL_INJECTION', 'true').lower() == 'true'
        self.enable_xss: bool = os.environ.get('ENABLE_XSS', 'true').lower() == 'true'
        self.enable_waf_bypass: bool = os.environ.get('ENABLE_WAF_BYPASS', 'true').lower() == 'true'
        self.enable_wordlist_update: bool = os.environ.get('ENABLE_WORDLIST_UPDATE', 'false').lower() == 'true'
        self.enable_telegram: bool = os.environ.get('ENABLE_TELEGRAM', 'false').lower() == 'true'
        self.enable_encryption: bool = os.environ.get('ENABLE_ENCRYPTION', 'false').lower() == 'true'
        self.enable_mfa_bypass: bool = os.environ.get('ENABLE_MFA_BYPASS', 'false').lower() == 'true'
        self.enable_enumeration: bool = os.environ.get('ENABLE_ENUMERATION', 'true').lower() == 'true'
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            'target_url': self.target_url,
            'username': self.username,
            'wordlist_path': self.wordlist_path,
            'features': {
                'bruteforce': self.enable_bruteforce,
                'sql_injection': self.enable_sql_injection,
                'xss': self.enable_xss,
                'waf_bypass': self.enable_waf_bypass,
                'wordlist_update': self.enable_wordlist_update,
                'telegram': self.enable_telegram,
                'encryption': self.enable_encryption,
                'mfa_bypass': self.enable_mfa_bypass,
                'enumeration': self.enable_enumeration
            }
        }
    
    def validate(self) -> bool:
        """Validate configuration"""
        errors: List[str] = []
        
        if self.enable_bruteforce and not self.wordlist_path:
            errors.append("Wordlist path required for bruteforce")
            
        if self.enable_bruteforce and self.captcha_url and not self.captcha_api_key:
            errors.append("Captcha API key required when captcha URL is set")
            
        if self.enable_telegram and (not self.telegram_bot_token or not self.telegram_chat_id):
            errors.append("Telegram bot token and chat ID required for notifications")
            
        if self.enable_encryption and not self.encryption_key:
            errors.append("Encryption key required for result encryption")
            
        if errors:
            print("\n[!] Configuration Errors:")
            for error in errors:
                print(f"    - {error}")
            return False
            
        return True
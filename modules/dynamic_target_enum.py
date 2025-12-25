import requests
import logging
import os
from urllib.parse import urljoin
from typing import List, Dict, Any

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

logging.basicConfig(filename='logs/results.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enumerate_targets(base_url: str) -> List[Dict[str, Any]]:
    """
    Enumerate common web application endpoints.
    
    Args:
        base_url: Base URL of the target (e.g., http://example.com)
        
    Returns:
        list: List of discovered endpoints with their status codes
    """
    # Comprehensive list of common endpoints
    endpoints = [
        # Admin panels
        "/admin", "/administrator", "/admin.php", "/admin/login", "/admin/dashboard",
        "/wp-admin", "/cpanel", "/phpmyadmin", "/adminer", "/adminpanel",
        
        # Authentication
        "/login", "/signin", "/login.php", "/auth", "/authenticate", "/user/login",
        "/account/login", "/users/login", "/session/new", "/sign-in",
        
        # Dashboards
        "/dashboard", "/panel", "/console", "/home", "/portal",
        
        # API endpoints
        "/api", "/api/v1", "/api/v2", "/rest", "/graphql", "/api/users", "/api/auth",
        
        # Configuration and debug
        "/config", "/debug", "/test", "/phpinfo.php", "/.env", "/config.php",
        "/settings", "/configuration",
        
        # Common files
        "/robots.txt", "/sitemap.xml", "/.git/config", "/.htaccess",
        "/web.config", "/composer.json", "/package.json",
        
        # Database
        "/db", "/database", "/mysql", "/phpmyadmin", "/adminer.php",
        
        # Backup files
        "/backup", "/backups", "/backup.sql", "/dump.sql", "/backup.zip",
        
        # Upload directories
        "/upload", "/uploads", "/files", "/media", "/images", "/assets"
    ]
    
    discovered: List[Dict[str, Any]] = []
    
    logging.info(f"Starting endpoint enumeration for {base_url}")
    print(f"[*] Memulai enumerasi endpoint untuk {base_url}")
    print(f"[*] Memeriksa {len(endpoints)} endpoint...\n")
    
    for endpoint in endpoints:
        # Properly construct URL
        endpoint_str: str = str(endpoint)
        base_url_str: str = str(base_url)
        url: str = urljoin(base_url_str.rstrip('/') + '/', endpoint_str.lstrip('/'))
        
        try:
            response = requests.get(url, timeout=10, allow_redirects=False)
            status = response.status_code
            
            # Analyze response
            interesting: bool = False
            details: List[str] = []
            
            # Check for interesting status codes
            if status == 200:
                interesting = True
                details.append("OK")
            elif status == 301 or status == 302:
                interesting = True
                redirect_location = response.headers.get('Location', 'Unknown')
                details.append(f"Redirect to {redirect_location}")
            elif status == 401:
                interesting = True
                details.append("Requires Authentication")
            elif status == 403:
                interesting = True
                details.append("Forbidden (exists but no access)")
            
            # Check content length
            content_length = len(response.content)
            if content_length > 0:
                details.append(f"{content_length} bytes")
            
            # Check for interesting headers
            if 'Server' in response.headers:
                details.append(f"Server: {response.headers['Server']}")
            
            # Log and display discovered endpoints
            if interesting:
                detail_str: str = " | ".join(details)
                endpoint_dict: Dict[str, Any] = {
                    'url': url,
                    'status': status,
                    'details': detail_str
                }
                discovered.append(endpoint_dict)
                
                logging.info(f"Endpoint found: {url} - Status: {status} - {detail_str}")
                print(f"[+] Endpoint ditemukan: {url}")
                print(f"    Status: {status} | {detail_str}\n")
                
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout accessing {url}")
            print(f"[!] Timeout: {url}")
        except requests.exceptions.ConnectionError:
            logging.warning(f"Connection error accessing {url}")
            print(f"[!] Connection Error: {url}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error accessing {url}: {e}")
            print(f"[!] Request Error ({url}): {e}")
        except Exception as e:
            logging.error(f"Unexpected error accessing {url}: {e}")
            print(f"[!] Unexpected Error ({url}): {e}")
    
    # Summary
    logging.info(f"Enumeration complete. Found {len(discovered)} interesting endpoints")
    print(f"\n[*] Enumerasi selesai. Ditemukan {len(discovered)} endpoint menarik dari {len(endpoints)} yang diperiksa")
    
    return discovered
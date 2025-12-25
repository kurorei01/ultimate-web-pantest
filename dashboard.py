#!/usr/bin/env python3
"""
Interactive dashboard and lobby system
"""

import sys
import time
from typing import Dict, Any
from config import Config
from notifier import VulnerabilityNotifier
from scanner import DynamicScanner
from ui import Menu, Animations, StatusDisplay, Colors
from modules.bruteforce import start_bruteforce

class InteractiveDashboard:
    """Main interactive dashboard"""
    
    def __init__(self) -> None:
        self.config = Config()
        self.notifier = VulnerabilityNotifier(self.config)
        self.scanner = DynamicScanner(self.config, self.notifier)
        self.running = True
    
    def show_config_menu(self) -> None:
        """Show configuration menu"""
        Menu.clear_screen()
        Menu.display_module_header("Configuration Settings", "⚙️")
        
        print(f"{Colors.OKCYAN}Current Configuration:{Colors.ENDC}\n")
        print(f"  Target URL: {Colors.YELLOW}{self.config.target_url}{Colors.ENDC}")
        print(f"  Username: {Colors.YELLOW}{self.config.username}{Colors.ENDC}")
        print(f"  Wordlist: {Colors.YELLOW}{self.config.wordlist_path}{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}Enabled Modules:{Colors.ENDC}\n")
        
        modules = {
            'Endpoint Enumeration': self.config.enable_enumeration,
            'SQL Injection': self.config.enable_sql_injection,
            'XSS Testing': self.config.enable_xss,
            'WAF Bypass': self.config.enable_waf_bypass,
            'Brute Force': self.config.enable_bruteforce,
            'MFA Bypass': self.config.enable_mfa_bypass,
            'Telegram Notifications': self.config.enable_telegram,
        }
        
        for module, enabled in modules.items():
            status = f"{Colors.OKGREEN}✓ Enabled{Colors.ENDC}" if enabled else f"{Colors.FAIL}✗ Disabled{Colors.ENDC}"
            print(f"  {module:<25} {status}")
        
        print(f"\n{Colors.WARNING}Note: Edit .env file to change configuration{Colors.ENDC}\n")
        
        input(f"{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_automated_scan(self) -> None:
        """Run automated full scan"""
        Menu.clear_screen()
        Menu.display_module_header("Automated Vulnerability Scan", "🔍")
        
        # Ask for target URL
        print(f"{Colors.GRAY}Current target: {self.config.target_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter target URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_url = custom_url.strip()
            self.config.target_login_url = f"{custom_url.strip()}/login.php"
            self.config.target_search_url = f"{custom_url.strip()}/search.php"
            self.config.target_contact_url = f"{custom_url.strip()}/contact.php"
            self.config.target_admin_url = f"{custom_url.strip()}/admin"
            self.config.target_mfa_url = f"{custom_url.strip()}/mfa"
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        # Confirm scan
        print(f"\n{Colors.YELLOW}Target: {self.config.target_url}{Colors.ENDC}")
        if not Menu.confirm("Start automated scan?"):
            return
        
        print()
        Animations.loading_animation("Initializing scanner", 2.0)
        
        # Run comprehensive scan
        results: Dict[str, Dict[str, Any]] = self.scanner.run_comprehensive_scan()
        
        # Display results
        print()
        StatusDisplay.display_summary_table(results)
        
        # Generate report
        self.notifier.generate_report()
        self.notifier.send_summary()
        
        StatusDisplay.success("Scan completed! Report saved to vulnerability_report.json")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_endpoint_enum(self) -> None:
        """Run endpoint enumeration only"""
        Menu.clear_screen()
        Menu.display_module_header("Endpoint Enumeration", "📡")
        
        # Ask for target URL
        print(f"{Colors.GRAY}Current target: {self.config.target_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter target URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_url = custom_url.strip()
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        print()
        result = self.scanner.scan_endpoints()
        
        print()
        if result['count'] > 0:
            StatusDisplay.success(f"Discovered {result['count']} endpoints")
        else:
            StatusDisplay.warning("No interesting endpoints found")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_sqli_scan(self) -> None:
        """Run SQL injection scan only"""
        Menu.clear_screen()
        Menu.display_module_header("SQL Injection Testing", "💉")
        
        # Ask for target URL
        print(f"{Colors.GRAY}Current target: {self.config.target_search_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter target URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_search_url = custom_url.strip()
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        # Ask for parameter to test
        print(f"\n{Colors.GRAY}Current parameter: {self.config.sql_param}{Colors.ENDC}")
        custom_param = Menu.get_user_choice("Enter parameter name (or press Enter to use default)")
        
        if custom_param and custom_param.strip():
            self.config.sql_param = custom_param.strip()
            StatusDisplay.success(f"Parameter updated to: {custom_param.strip()}")
        
        print()
        result = self.scanner.scan_sql_injection()
        
        print()
        if result['success']:
            StatusDisplay.error(f"Found {result['count']} SQL injection vulnerabilities!")
        else:
            StatusDisplay.success("No SQL injection vulnerabilities found")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_xss_scan(self) -> None:
        """Run XSS scan only"""
        Menu.clear_screen()
        Menu.display_module_header("XSS Vulnerability Scan", "🚨")
        
        # Ask for target URL
        print(f"{Colors.GRAY}Current target: {self.config.target_contact_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter target URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_contact_url = custom_url.strip()
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        # Ask for parameter to test
        print(f"\n{Colors.GRAY}Current parameter: {self.config.xss_param}{Colors.ENDC}")
        custom_param = Menu.get_user_choice("Enter parameter name (or press Enter to use default)")
        
        if custom_param and custom_param.strip():
            self.config.xss_param = custom_param.strip()
            StatusDisplay.success(f"Parameter updated to: {custom_param.strip()}")
        
        print()
        result = self.scanner.scan_xss()
        
        print()
        if result['success']:
            StatusDisplay.error(f"Found {result['count']} XSS vulnerabilities!")
        else:
            StatusDisplay.success("No XSS vulnerabilities found")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_bruteforce(self) -> None:
        """Run brute force attack"""
        Menu.clear_screen()
        Menu.display_module_header("Brute Force Attack", "🔐")
        
        if not self.config.enable_bruteforce:
            StatusDisplay.error("Brute force module is disabled in configuration")
            input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
            return
        
        # Ask for login URL
        print(f"{Colors.GRAY}Current target: {self.config.target_login_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter login URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_login_url = custom_url.strip()
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        # Ask for username
        print(f"\n{Colors.GRAY}Current username: {self.config.username}{Colors.ENDC}")
        custom_username = Menu.get_user_choice("Enter username (or press Enter to use default)")
        
        if custom_username and custom_username.strip():
            self.config.username = custom_username.strip()
            StatusDisplay.success(f"Username updated to: {custom_username.strip()}")
        
        print()
        StatusDisplay.info(f"Target: {self.config.target_login_url}")
        StatusDisplay.info(f"Username: {self.config.username}")
        StatusDisplay.info(f"Wordlist: {self.config.wordlist_path}")
        
        if not Menu.confirm("\nStart brute force attack?"):
            return
        
        print()
        try:
            start_bruteforce(
                url=self.config.target_login_url,
                username=self.config.username,
                wordlist_path=self.config.wordlist_path,
                captcha_url=self.config.captcha_url,
                api_key=self.config.captcha_api_key
            )
        except Exception as e:
            StatusDisplay.error(f"Brute force error: {e}")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_waf_bypass(self) -> None:
        """Run WAF bypass testing"""
        Menu.clear_screen()
        Menu.display_module_header("WAF Bypass Testing", "🛡️")
        
        # Ask for target URL
        print(f"{Colors.GRAY}Current target: {self.config.target_admin_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter target URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_admin_url = custom_url.strip()
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        print()
        result = self.scanner.scan_waf_bypass()
        
        print()
        if result['success']:
            StatusDisplay.error(f"WAF bypassed {result['count']} times!")
        else:
            StatusDisplay.success("WAF is properly configured")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run_mfa_bypass(self) -> None:
        """Run MFA bypass testing"""
        Menu.clear_screen()
        Menu.display_module_header("MFA Bypass Testing", "🔑")
        
        if not self.config.enable_mfa_bypass:
            StatusDisplay.error("MFA bypass module is disabled in configuration")
            input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
            return
        
        # Ask for MFA URL
        print(f"{Colors.GRAY}Current target: {self.config.target_mfa_url}{Colors.ENDC}")
        custom_url = Menu.get_user_choice("Enter MFA endpoint URL (or press Enter to use default)")
        
        if custom_url and custom_url.strip():
            self.config.target_mfa_url = custom_url.strip()
            StatusDisplay.success(f"Target updated to: {custom_url.strip()}")
        
        print()
        StatusDisplay.info("Testing common MFA bypass techniques...")
        # Implementation would go here
        
        StatusDisplay.warning("MFA bypass testing not yet implemented")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def view_results(self) -> None:
        """View previous scan results"""
        Menu.clear_screen()
        Menu.display_module_header("Previous Results", "📊")
        
        if self.notifier.stats['total'] == 0:
            StatusDisplay.warning("No vulnerabilities found in current session")
        else:
            print(f"\n{Colors.BOLD}Vulnerability Statistics:{Colors.ENDC}\n")
            print(f"  🔴 Critical: {self.notifier.stats['critical']}")
            print(f"  🟠 High: {self.notifier.stats['high']}")
            print(f"  🟡 Medium: {self.notifier.stats['medium']}")
            print(f"  🟢 Low: {self.notifier.stats['low']}")
            print(f"  ℹ️  Info: {self.notifier.stats['info']}")
            print(f"\n  📊 Total: {self.notifier.stats['total']}")
        
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
    
    def run(self) -> None:
        """Run interactive dashboard"""
        # Validate config
        if not self.config.validate():
            StatusDisplay.error("Invalid configuration. Please check your .env file")
            sys.exit(1)
        
        while self.running:
            Menu.display_main_menu()
            
            choice = Menu.get_user_choice("Enter your choice")
            
            if choice == '1':
                self.run_automated_scan()
            elif choice == '2':
                self.run_endpoint_enum()
            elif choice == '3':
                self.run_sqli_scan()
            elif choice == '4':
                self.run_xss_scan()
            elif choice == '5':
                self.run_bruteforce()
            elif choice == '6':
                self.run_waf_bypass()
            elif choice == '7':
                self.run_mfa_bypass()
            elif choice == '8':
                self.show_config_menu()
            elif choice == '9':
                self.view_results()
            elif choice == '0':
                Menu.clear_screen()
                Animations.typewriter_effect(f"\n{Colors.OKGREEN}Thank you for using Ultimate Web Pentest Framework!{Colors.ENDC}")
                Animations.typewriter_effect(f"{Colors.OKCYAN}Stay safe, hack responsibly! 🛡️{Colors.ENDC}\n")
                self.running = False
            else:
                StatusDisplay.error("Invalid choice. Please try again.")
                time.sleep(1)
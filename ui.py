#!/usr/bin/env python3
"""
Interactive UI Module with animations and menus
"""

import time
import sys
from typing import Dict, Any
from datetime import datetime

class Colors:
    """ANSI color codes"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Additional colors
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'

class Animations:
    """ASCII animations and effects"""
    
    @staticmethod
    def print_banner() -> None:
        """Print animated banner"""
        banner = f"""
{Colors.OKCYAN}
╦ ╦╦ ╔╦╗╦╔╦╗╔═╗╔╦╗╔═╗  ╦ ╦╔═╗╔╗ 
║ ║║  ║ ║║║║╠═╣ ║ ║╣   ║║║║╣ ╠╩╗
╚═╝╩═╝╩ ╩╩ ╩╩ ╩ ╩ ╚═╝  ╚╩╝╚═╝╚═╝
                                 
╔═╗╔═╗╔╗╔╔╦╗╔═╗╔═╗╔╦╗            
╠═╝║╣ ║║║ ║ ║╣ ╚═╗ ║             
╩  ╚═╝╝╚╝ ╩ ╚═╝╚═╝ ╩             
{Colors.ENDC}
{Colors.WARNING}╔═══════════════════════════════════════════════════════╗
║  Advanced Web Penetration Testing Framework v2.0   ║
║  Automated Security Assessment Tool                ║
╚═══════════════════════════════════════════════════════╝{Colors.ENDC}
"""
        for line in banner.split('\n'):
            print(line)
            time.sleep(0.05)
    
    @staticmethod
    def loading_animation(text: str = "Loading", duration: float = 2.0) -> None:
        """Show loading animation"""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for char in chars:
                sys.stdout.write(f'\r{Colors.OKCYAN}{char}{Colors.ENDC} {text}...')
                sys.stdout.flush()
                time.sleep(0.1)
        
        sys.stdout.write('\r' + ' ' * (len(text) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def progress_bar(current: int, total: int, text: str = "", width: int = 50) -> None:
        """Show progress bar"""
        percent = current / total if total > 0 else 0
        filled = int(width * percent)
        bar = '█' * filled + '░' * (width - filled)
        
        sys.stdout.write(f'\r{Colors.OKBLUE}[{bar}] {percent*100:.1f}% {text}{Colors.ENDC}')
        sys.stdout.flush()
        
        if current >= total:
            print()
    
    @staticmethod
    def typewriter_effect(text: str, delay: float = 0.03) -> None:
        """Print text with typewriter effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

class Menu:
    """Interactive menu system"""
    
    @staticmethod
    def clear_screen() -> None:
        """Clear terminal screen"""
        print("\033[H\033[J", end="")
    
    @staticmethod
    def display_main_menu() -> None:
        """Display main menu"""
        Menu.clear_screen()
        Animations.print_banner()
        
        print(f"\n{Colors.BOLD}{Colors.OKGREEN}╔═══════════════════ MAIN MENU ═══════════════════════╗{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║                                                      ║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[1]{Colors.ENDC} 🔍 Automated Scan (All Modules)            {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[2]{Colors.ENDC} 📡 Endpoint Enumeration                     {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[3]{Colors.ENDC} 💉 Auto SQL Injection (Advanced)            {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[4]{Colors.ENDC} 🚨 Auto XSS Scanner (Advanced)              {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[5]{Colors.ENDC} 🔐 Brute Force Attack                       {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[6]{Colors.ENDC} 🛡️  WAF Bypass Attempts                      {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[7]{Colors.ENDC} 🔑 MFA Bypass Testing                       {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[8]{Colors.ENDC} ⚙️  Configuration Settings                   {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[9]{Colors.ENDC} 📊 View Previous Results                    {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║  {Colors.OKCYAN}[0]{Colors.ENDC} ❌ Exit                                      {Colors.OKGREEN}║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║                                                      ║{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.OKGREEN}╚══════════════════════════════════════════════════════╝{Colors.ENDC}\n")
    
    @staticmethod
    def get_user_choice(prompt: str = "Select option") -> str:
        """Get user input with styled prompt"""
        return input(f"{Colors.BOLD}{Colors.OKCYAN}[?] {prompt}: {Colors.ENDC}")
    
    @staticmethod
    def confirm(message: str) -> bool:
        """Ask for confirmation"""
        response = input(f"{Colors.WARNING}[?] {message} (y/n): {Colors.ENDC}").lower()
        return response in ['y', 'yes']
    
    @staticmethod
    def display_module_header(module_name: str, icon: str = "🔧") -> None:
        """Display module header"""
        Menu.clear_screen()
        print(f"\n{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}{icon}  {module_name.upper()}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}{'=' * 60}{Colors.ENDC}\n")

class StatusDisplay:
    """Real-time status display"""
    
    @staticmethod
    def success(message: str) -> None:
        """Print success message"""
        print(f"{Colors.OKGREEN}[✓] {message}{Colors.ENDC}")
    
    @staticmethod
    def error(message: str) -> None:
        """Print error message"""
        print(f"{Colors.FAIL}[✗] {message}{Colors.ENDC}")
    
    @staticmethod
    def warning(message: str) -> None:
        """Print warning message"""
        print(f"{Colors.WARNING}[!] {message}{Colors.ENDC}")
    
    @staticmethod
    def info(message: str) -> None:
        """Print info message"""
        print(f"{Colors.OKCYAN}[i] {message}{Colors.ENDC}")
    
    @staticmethod
    def vulnerability_found(vuln_type: str, severity: str, details: str) -> None:
        """Display vulnerability found"""
        severity_colors = {
            'CRITICAL': Colors.FAIL,
            'HIGH': Colors.WARNING,
            'MEDIUM': Colors.YELLOW,
            'LOW': Colors.OKBLUE,
            'INFO': Colors.GRAY
        }
        
        color = severity_colors.get(severity, Colors.WHITE)
        
        print(f"\n{color}{'=' * 60}")
        print(f"🚨 VULNERABILITY DETECTED!")
        print(f"Type: {vuln_type}")
        print(f"Severity: {severity}")
        print(f"Details: {details}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'=' * 60}{Colors.ENDC}\n")
    
    @staticmethod
    def display_summary_table(results: Dict[str, Dict[str, Any]]) -> None:
        """Display results in table format"""
        print(f"\n{Colors.BOLD}{Colors.OKGREEN}╔════════════════════ TEST SUMMARY ════════════════════╗{Colors.ENDC}")
        print(f"{Colors.OKGREEN}║ Module                    │ Status    │ Found      ║{Colors.ENDC}")
        print(f"{Colors.OKGREEN}╠═══════════════════════════╪═══════════╪════════════╣{Colors.ENDC}")
        
        for module, data in results.items():
            module_str: str = str(module)
            success: bool = bool(data.get('success', False))
            status_icon: str = "✓" if success else "✗"
            status_color: str = Colors.OKGREEN if success else Colors.FAIL
            count: int = int(data.get('count', 0))
            status_text: str = str(data.get('status', 'N/A'))
            
            module_display: str = f"{module_str:<25}"
            status_display: str = f"{status_icon} {status_text:<7}"
            count_display: str = f"{count:<10}"
            
            print(f"{Colors.OKGREEN}║ {Colors.ENDC}{module_display} │ {status_color}{status_display}{Colors.ENDC} │ {count_display} {Colors.OKGREEN}║{Colors.ENDC}")
        
        print(f"{Colors.BOLD}{Colors.OKGREEN}╚══════════════════════════════════════════════════════╝{Colors.ENDC}\n")
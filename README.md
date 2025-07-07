🌐 WebExposureCheck - Website Exposure Scanner  
📌 Author: Mohammed  |  x: @m7mdatd  
🔧 Version: 1.0  
🛠️  This tool scans for exposed files and directories...

**WebExposureCheck** is a lightweight Python tool designed to scan websites for publicly exposed files and sensitive paths. It’s a handy tool for ethical hackers, penetration testers, and sysadmins to check common misconfigurations in web deployments.

---

## 🔍 What It Checks

The tool scans for common exposed paths such as:

- `.git/` repositories  
- `.env` environment files  
- Backup files (`.bak`, `.zip`, `.tar.gz`)  
- PHP info files (`phpinfo.php`)  
- Admin/control panels (`/admin`, `/cpanel`)  
- Configuration files (`config.php`, `wp-config.php.bak`)  
- Debug logs and more...

---

## 🚀 How to Use

### 📦 Prerequisites

Install the required libraries:

```bash
git clone https://github.com/m7mdatd/WebExposureCheck.git
cd WebExposureCheck
python3 web_exposure_check.py example.com

🔍 Scanning: http://example.com/

[+] Found: http://example.com/.git/
[-] Forbidden (403): http://example.com/admin/
[!] Connection error: http://example.com/debug.log

⚠️ Legal Disclaimer
This tool is intended for authorized security testing and educational purposes only.
Unauthorized scanning or usage on websites you don’t own is illegal.

📁 Project Structure
bash

web_exposure_check.py     # Main script
README.md                 # Documentation
requirements.txt          # (Optional) Python dependencies


📃 License
MIT License – feel free to use and contribute.

✨ Contributions
Feel free to fork the project, submit issues or open pull requests.
Let's make the web a safer place together!

👨‍💻 Author
Developed by Mohammed
x: @m7mdatd

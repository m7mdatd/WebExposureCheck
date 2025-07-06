#!/usr/bin/env python3
# WebExposureCheck v1.0
# A tool to check public exposure to sensitive files on websites.

import requests
import sys
from colorama import Fore, Style

COMMON_PATHS = [
    ".git/", ".env", "backup.zip", "db.sql", "phpinfo.php", "admin/", "cpanel/", 
    "config.php", "config.bak", "wp-config.php.bak", "debug.log"
]

def check_url(base_url):
    if not base_url.startswith("http"):
        base_url = "http://" + base_url
    if not base_url.endswith("/"):
        base_url += "/"
    print(f"\n🔍 Site inspection: {base_url}\n")

    for path in COMMON_PATHS:
        full_url = base_url + path
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code == 200 and len(r.text) > 20:
                print(Fore.GREEN + f"[+] was found: {full_url}" + Style.RESET_ALL)
            elif r.status_code == 403:
                print(Fore.YELLOW + f"[-] rejected (403): {full_url}" + Style.RESET_ALL)
            elif r.status_code == 401:
                print(Fore.YELLOW + f"[-] Requires login (401): {full_url}" + Style.RESET_ALL)
        except requests.exceptions.RequestException:
            print(Fore.RED + f"[!] Communication error: {full_url}" + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python3 web_exposure_check.py example.com")
        sys.exit(1)
    check_url(sys.argv[1])

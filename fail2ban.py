import os
import re
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def print_header(title):
    print(Fore.GREEN + Style.BRIGHT + f"{title}")
    print(Fore.GREEN + '-' * len(title))
    print()

def print_footer(message, success=True):
    if success:
        print(Fore.GREEN + Style.BRIGHT + message)
    else:
        print(Fore.RED + Style.BRIGHT + message)
    print()

def check_fail2ban_logs(log_file="/var/log/fail2ban.log"):
    if not os.path.exists(log_file):
        print_footer(f"Fail2Ban log file not found: {log_file}", success=False)
        return
    
    print_header(f"Analyzing Fail2Ban Logs: {log_file}")
    
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # Patterns to look for in the logs
    fail_pattern = re.compile(r"fail(?:ed|ure)?\s+.*\s+(\d{3}\.\d{3}\.\d{3}\.\d{3})")
    ban_pattern = re.compile(r"Ban\s+(\d{3}\.\d{3}\.\d{3}\.\d{3})")
    
    failed_attempts = {}
    banned_ips = {}

    for line in logs:
        # Find failed attempts
        fail_match = fail_pattern.search(line)
        if fail_match:
            ip = fail_match.group(1)
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

        # Find bans
        ban_match = ban_pattern.search(line)
        if ban_match:
            ip = ban_match.group(1)
            if ip in banned_ips:
                banned_ips[ip] += 1
            else:
                banned_ips[ip] = 1

    # Print report
    print(Fore.YELLOW + "Failed Login Attempts:")
    for ip, count in failed_attempts.items():
        print(f"IP: {ip} - Failed Attempts: {count}")

    print()
    print(Fore.YELLOW + "Banned IPs:")
    for ip, count in banned_ips.items():
        print(f"IP: {ip} - Bans: {count}")

    # Look for unusual patterns
    print()
    print(Fore.YELLOW + "Unusual Patterns:")
    for ip in failed_attempts:
        if failed_attempts[ip] > 10 and ip not in banned_ips:
            print(Fore.RED + f"Potential vulnerability: {ip} has {failed_attempts[ip]} failed attempts but is not banned!")

    print_footer("Fail2Ban Log Analysis Completed [ OK ]")

if __name__ == "__main__":
    check_fail2ban_logs()

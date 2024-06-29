import os
import sys
import subprocess
from colorama import Fore, Back, Style, init

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

def dir_clamav(scan_path):
    print_header(f"Scanning Directory with ClamAV: {scan_path}")
    scan_command = f"sudo clamscan --remove --recursive --infected {scan_path}"
    scan = os.popen(scan_command).read()
    print(scan)
    print_footer("ClamAV Scan Completed [ OK ]")

def rkhunter():
    print_header("Starting System Scan with RootKitHunter")
    result = subprocess.run(['sudo', 'rkhunter', '--check'], capture_output=True, text=True)
    print(result.stdout)
    
    if result.returncode == 0:
        print_footer("System Scanned with RootKitHunter [ OK ]")
    else:
        print_footer("RootKit Scan System [ ERROR ]", success=False)

def vul_check():
    print_header("Checking System Vulnerabilities with Lynis")
    vul_command = "sudo lynis audit system"
    vul = os.popen(vul_command).read()
    print(vul)
    print_footer("System Vulnerability Check Done with Lynis [ OK ]")

def full_clamav():
    print_header("Performing Full System Scan")
    
    clamascan_command = "sudo clamscan --remove --infected --recursive /"
    rkhunter_command = "sudo rkhunter -c"
    
    print_header("ClamAV Scan in Progress")
    clamascan = os.popen(clamascan_command).read()
    print(clamascan)
    
    print_header("RootKitHunter Scan in Progress")
    rkhunter = os.popen(rkhunter_command).read()
    print(rkhunter)
    
    print_header("Checking Vulnerabilities")
    print(vul_check())
    
    print_footer("Full System Scan Completed [ OK ]")



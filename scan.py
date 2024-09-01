import os
import subprocess
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






def dir_clamav(scan_path):
    print_header(f"Scanning Directory with ClamAV: {scan_path}")
    scan_command = f"sudo clamscan --remove --recursive --infected {scan_path}"
    scan = os.popen(scan_command).read()
    print(scan)
    print_footer("ClamAV Scan Completed [ OK ]")

def rkhunter():
    print_header("Starting System Scan with RootKitHunter and chkrootkit")
    
    # Run rkhunter
    rkhunter_result = subprocess.run(['sudo', 'rkhunter', '--check', '--skip-keypress'], capture_output=True, text=True)
    print(rkhunter_result.stdout)
    
    # Run chkrootkit
    chkrootkit_result = subprocess.run(['sudo', 'chkrootkit'], capture_output=True, text=True)
    print(chkrootkit_result.stdout)
    
    # Evaluate results
    if "No malware detected" in rkhunter_result.stdout and chkrootkit_result.returncode == 0:
        print_footer("System Scanned with RootKitHunter and chkrootkit [ OK ]")
    else:
        print_footer("RootKitHunter or chkrootkit Detected Issues [ ERROR ]", success=False)

def vul_check():
    print_header("Checking System Vulnerabilities with Lynis")
    vul_command = "sudo lynis audit system"
    vul = os.popen(vul_command).read()
    print(vul)
    print_footer("System Vulnerability Check Done with Lynis [ OK ]")

def full_clamav():
    print_header("Performing Full System Scan")
    
    # Run ClamAV scan
    print_header("ClamAV Scan in Progress")
    clamascan_command = "sudo clamscan --remove --infected --recursive /"
    clamascan = os.popen(clamascan_command).read()
    print(clamascan)
    
    print_header("maldet in Progress")
    maldet_command = "sudo maldet -a"
    maldet = os.popen(maldet_command).read()
    print(maldet)
    # Run RootKitHunter scan
    print_header("RootKitHunter Scan in Progress")
    rkhunter()
    
    # Run Lynis vulnerability check
    print_header("Checking Vulnerabilities")
    vul_check()
    
    print_footer("Full System Scan Completed [ OK ]")


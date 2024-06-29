import os
import sys
from colorama import Fore, Back, Style, init
import re

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

def colorize_output(output):
    """
    Apply color to the output based on certain patterns.
    """
    # Example patterns and their colors
    patterns = {
        r'(\s+\w+\.service)': Fore.CYAN,  # Service names
        r'(running|exited|failed)': Fore.GREEN,  # Statuses
    }
    
    for pattern, color in patterns.items():
        output = re.sub(pattern, lambda x: color + x.group(0) + Fore.RESET, output)
    
    return output

def service():
    print_header("Listing Services")
    s = os.popen("sudo systemctl list-units --type=service").read()
    colored_s = colorize_output(s)
    print(colored_s)
    print_footer("Services Listed [ OK ]")

def start_service():
    if len(sys.argv) < 4:
        print(Fore.RED + "Error: Service name is required.")
        return
    service_name = sys.argv[3]
    print_header(f"Starting Service: {service_name}")
    start = os.popen(f"sudo systemctl start {service_name}").read()
    print(start)
    print_footer(f"Service '{service_name}' Started [ OK ]")

def stop_service():
    if len(sys.argv) < 4:
        print(Fore.RED + "Error: Service name is required.")
        return
    service_name = sys.argv[3]
    print_header(f"Stopping Service: {service_name}")
    stop = os.popen(f"sudo systemctl stop {service_name}").read()
    print(stop)
    print_footer(f"Service '{service_name}' Stopped [ OK ]", success=True)

def restart():
    if len(sys.argv) < 4:
        print(Fore.RED + "Error: Service name is required.")
        return
    service_name = sys.argv[3]
    print_header(f"Restarting Service: {service_name}")
    restart = os.popen(f"sudo systemctl restart {service_name}").read()
    print(restart)
    print_footer(f"Service '{service_name}' Restarted [ OK ]", success=True)


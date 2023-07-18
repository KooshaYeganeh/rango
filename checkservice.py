import os
import sys
from colorama import Fore, Back, Style



def service():
    s = os.popen("sudo systemctl list-units --type=service").read()
    print(s)
    return "Service Listed [ OK ]"




def start_service():
    service_name = sys.argv[3]
    start = os.popen(f"sudo systemctl start {service_name}").read()
    print(start)
    print(Fore.CYAN + "service"  + Fore.RESET + " Started [ OK ]")
    return " "



def stop_service():
    service_name = sys.argv[3]
    stop = os.popen(f"sudo systemctl stop {service_name}").read()
    print(stop)
    print(Fore.RED + "service" + Fore.RESET + " stopted [ OK ]")
    
    return " "



def restart():
    service_name = sys.argv[3]
    restart = os.popen(f"sudo systemctl restart {service_name}").read()
    
    print(Fore.CYAN + "service"  + Fore.RESET + "restarted [ OK ]")
    print(restart)

    return " "







from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def help():
    print(f"{Fore.CYAN}Usage: {Style.BRIGHT}rango <command> [options]{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Commands:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--encrypt, -E{Style.RESET_ALL}        {Fore.WHITE}Encrypt files in a directory{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--sort, -S{Style.RESET_ALL}           {Fore.WHITE}Sort files in a directory{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--scan, -SS{Style.RESET_ALL}          {Fore.WHITE}Scan options{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--firewall, -FW{Style.RESET_ALL}      {Fore.WHITE}Firewall options{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--checkport, -CP{Style.RESET_ALL}     {Fore.WHITE}Check open ports{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--service{Style.RESET_ALL}            {Fore.WHITE}Service options{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--monitor{Style.RESET_ALL}            {Fore.WHITE}Monitor options{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}--help, -H{Style.RESET_ALL}           {Fore.WHITE}Display this help message{Style.RESET_ALL}")

def encrypt_help():
    print(f"{Fore.MAGENTA}Encrypt{Style.RESET_ALL}")
    print(f"{Fore.CYAN}rango --encrypt DIRECTORY or rango -E DIRECTORY{Style.RESET_ALL}")
    print(f"\t{Fore.WHITE}Example : ➜  rango --encrypt /tmp/Koosha{Style.RESET_ALL}")

def sort_help():
    print(f"{Fore.MAGENTA}Sort : Sort Files in Given Directory{Style.RESET_ALL}")
    print(f"{Fore.CYAN}rango --sort DIRECTORY{Style.RESET_ALL}")
    print(f"\t{Fore.WHITE}Example : ➜  rango --sort /home/koosha/Desktop{Style.RESET_ALL}")

def scan_help():
    print(f"{Fore.MAGENTA}Scan{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Full Scan : Full Scan of System with ClamAV and RKHunter and Lynis{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --scan --full{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -SS -F{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --scan --dir /home/koosha/Downloads{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -SS -D /home/koosha/Downloads{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --scan --rootkit{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -SS -RK{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --scan --vul{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -SS -VUL{Style.RESET_ALL}")

def firewall_help():
    print(f"{Fore.MAGENTA}FireWall{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}WebServer : add Firewall configs For WebServer Automatically{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --firewall --webserver{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -FW -WB{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}Check : check Firewall configs{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --firewal --check{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -FW -C{Style.RESET_ALL}")

def service_help():
    print(f"{Fore.MAGENTA}Service{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}Service check : List Service and start & stop & restart Services{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --service --list{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --service start SERVICE_NAME{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --service stop SERVICE_NAME{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --service restart SERVICE_NAME{Style.RESET_ALL}")

def port_help():
    print(f"{Fore.MAGENTA}Port{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}Check Ports : check open ports{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango --checkport --result{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}➜  rango -CP -R{Style.RESET_ALL}")

def all():
    help()
    print()
    encrypt_help()
    print()
    sort_help()
    print()
    scan_help()
    print()
    firewall_help()
    print()
    service_help()
    print()
    port_help()


import socket
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def check_port(host, port):
    """Check if a port is open on a given host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)  # Adjust the timeout as needed
            result = sock.connect_ex((host, port))
        return result == 0
    except socket.error as e:
        print(Fore.LIGHTRED_EX + f"Socket error: {e}")
        return False

def show_port():
    """Check and display the status of specified ports on a host."""
    host = '127.0.0.1'  # Replace with the target host or IP address
    ports = [80, 443, 22, 23, 21, 53, 3306, 389, 636, 444, 445]  # Specify the ports to check

    print(Fore.LIGHTCYAN_EX + "Checking ports on host:", host)
    print(Fore.LIGHTYELLOW_EX + "Port Status")
    print(Fore.LIGHTYELLOW_EX + "-" * 30)

    results = []
    for port in ports:
        if check_port(host, port):
            results.append(f"{Fore.LIGHTGREEN_EX}Port {port} ➜ open")
        else:
            results.append(f"{Fore.LIGHTRED_EX}Port {port} ➜ closed")

    # Print all results
    for result in results:
        print(result)

    print(Style.RESET_ALL + "\nCheck All Ports [ OK ]")
    return "Check All Ports [ OK ]"

if __name__ == "__main__":
    show_port()


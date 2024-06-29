import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # Adjust the timeout as needed
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def show_port():
    host = '127.0.0.1'  # Replace with the target host or IP address
    ports = [80, 443, 22, 23, 21, 53, 3306, 389, 636, 444, 445]  # Specify the ports to check

    results = []
    for port in ports:
        if check_port(host, port):
            results.append(f"Port {port} ➜ open")
        else:
            results.append(f"Port {port} ➜ closed")

    # Print all results
    for result in results:
        print(result)

    return "check All Ports [ OK ]"


import os
import sys
import encrypt
import sort
import scan
import firewall
import manual
import checkport
import checkservice
import subprocess
import fail2ban

def main():
    if len(sys.argv) < 2:
        print("Usage: rango <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--encrypt" or command == "-E":
        if len(sys.argv) < 3:
            print("Error: Directory path is required for --encrypt")
            sys.exit(1)
        directory = sys.argv[2]
        encrypt.encrypt_file(directory)
        encrypt.encrypt_files_in_directory(directory, encrypt.key)
        print("All Files Encrypted [ OK ]")

    elif command == "--sort" or command == "-S":
        if len(sys.argv) < 3:
            print("Error: Directory path is required for --sort")
            sys.exit(1)
        directory = sys.argv[2]
        sort.sort_files(directory)
        print("Files Sorted [ OK ]")

    elif command == "--scan" or command == "-SS":
        if len(sys.argv) < 3:
            print("Error: Scan type is required for --scan")
            sys.exit(1)
        scan_type = sys.argv[2]
        scan_name = sys.argv[3]
        if scan_type == "--full" or scan_type == "-F":
            scan.full_clamav()
        elif scan_type == "--dir" or scan_type == "-D":
            if len(sys.argv) < 4:
                print("Error: Directory path is required for --scan --dir")
                sys.exit(1)
            directory = sys.argv[3]
            scan.dir_clamav(directory)
        elif scan_type == "--rootkit" or scan_type == "-RK":
            scan.rkhunter()
        elif scan_type == "--vul" or scan_type == "-VUL":
            if len(sys.argv) < 4:
                print("Error: Scan name is required for --scan --vul")
                sys.exit(1)
            scan_name = sys.argv[3]
            if scan_name == "--fail2ban" or scan_name == "-FB":
                fail2ban.check_fail2ban_logs()
            else:
                scan.vul_check()
        else:
            print("Invalid scan type.")
            sys.exit(1)

    elif command == "--firewall" or command == "-FW":
        if len(sys.argv) < 3:
            print("Error: Firewall action is required for --firewall")
            sys.exit(1)
        firewall_action = sys.argv[2]
        if firewall_action == "--webserver" or firewall_action == "-WB":
            firewall.set_webserver_firewall()
        elif firewall_action == "--check" or firewall_action == "-C":
            firewall.show_firewall_config()
        else:
            print("Invalid firewall action.")
            sys.exit(1)

    elif command == "--checkport" or command == "-CP":
        if len(sys.argv) < 3:
            print("Error: Checkport action is required for --checkport")
            sys.exit(1)
        port_action = sys.argv[2]
        if port_action == "--result" or port_action == "-R":
            checkport.show_port()
        else:
            print("Invalid checkport action.")
            sys.exit(1)

    elif command == "--service":
        if len(sys.argv) < 3:
            print("Error: Service action is required for --service")
            sys.exit(1)
        service_action = sys.argv[2]
        if service_action == "--list":
            checkservice.service()
        elif service_action == "--start":
            if len(sys.argv) < 4:
                print("Error: Service name is required for --service --start")
                sys.exit(1)
            service_name = sys.argv[3]
            checkservice.start_service(service_name)
        elif service_action == "--stop":
            if len(sys.argv) < 4:
                print("Error: Service name is required for --service --stop")
                sys.exit(1)
            service_name = sys.argv[3]
            checkservice.stop_service(service_name)
        elif service_action == "--restart":
            if len(sys.argv) < 4:
                print("Error: Service name is required for --service --restart")
                sys.exit(1)
            service_name = sys.argv[3]
            checkservice.restart(service_name)
        else:
            print("Invalid service action.")
            sys.exit(1)

    elif command == "--monitor":
        if len(sys.argv) < 3:
            print("Error: Monitor action is required for --monitor")
            sys.exit(1)
        monitor_action = sys.argv[2]
        if monitor_action == "--system":
            print("\n\nEnter command glances to Monitor system :)")
            print("➜ command : glances")
        else:
            print("Invalid monitor action.")
            sys.exit(1)

    elif command == "--help" or command == "-H":
        manual.help()
        if len(sys.argv) > 2:
            help_command = sys.argv[2]
            if help_command == "--scan" or help_command == "-SS":
                manual.scan_help()
            elif help_command == "--encrypt" or help_command == "-E":
                manual.encrypt_help()
            elif help_command == "--sort" or help_command == "-S":
                manual.sort_help()
            elif help_command == "--firewall" or help_command == "-FW":
                manual.firewall_help()
            elif help_command == "--service":
                manual.service_help()
            elif help_command == "--port":
                manual.port_help()
            elif help_command == "--all" or help_command == "-A":
                manual.all()
            else:
                print("Invalid help command.")
                sys.exit(1)
        else:
            manual.help()
            print("For more detailed help, use --help followed by a command.")

    else:
        print("Invalid command.")
        sys.exit(1)

if __name__ == "__main__":
    main()


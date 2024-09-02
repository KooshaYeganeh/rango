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

    if command in ["--encrypt", "-E"]:
        if len(sys.argv) < 3:
            print("Error: Directory path is required for --encrypt")
            sys.exit(1)
        directory = sys.argv[2]
        encrypt.encrypt_file(directory)
        encrypt.encrypt_files_in_directory(directory, encrypt.key)
        print("All Files Encrypted [ OK ]")

    elif command in ["--sort", "-S"]:
        if len(sys.argv) < 3:
            print("Error: Directory path is required for --sort")
            sys.exit(1)
        directory = sys.argv[2]
        sort.sort_files(directory)
        print("Files Sorted [ OK ]")

    elif command in ["--scan", "-SS"]:
        if len(sys.argv) < 3:
            print("Error: Scan type is required for --scan")
            sys.exit(1)
        scan_type = sys.argv[2]

        if scan_type in ["--full", "-F"]:
            scan.full_clamav()

        elif scan_type in ["--dir", "-D"]:
            if len(sys.argv) < 4:
                print("Error: Directory path is required for --scan --dir")
                sys.exit(1)
            directory = sys.argv[3]
            scan.dir_clamav(directory)

        elif scan_type in ["--rootkit", "-RK"]:
            scan.rkhunter()

        elif scan_type in ["--vul", "-VUL"]:
            scan.vul_check()    
        elif scan_type in ["--fail2ban", "-FB"]:
                fail2ban.check_fail2ban_logs()
        else:
            print("Invalid scan type.")
            sys.exit(1)

    elif command in ["--firewall", "-FW"]:
        if len(sys.argv) < 3:
            print("Error: Firewall action is required for --firewall")
            sys.exit(1)
        firewall_action = sys.argv[2]
        if firewall_action in ["--webserver", "-WB"]:
            firewall.set_webserver_firewall()
        elif firewall_action in ["--show", "-SH"]:
            firewall.show_firewall_config()
        elif firewall_action in ["--add", "-A"]:
            if len(sys.argv) < 4:
                print("Error: Firewall rule is required for --add")
                sys.exit(1)
            rule = sys.argv[3]
            print(firewall.add_rule(rule))
        else:
            print("Invalid firewall action.")
            sys.exit(1)

    elif command in ["--checkport", "-CP"]:
        if len(sys.argv) < 3:
            print("Error: Checkport action is required for --checkport")
            sys.exit(1)
        port_action = sys.argv[2]
        if port_action in ["--result", "-R"]:
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
        elif service_action == "--report":
            checkservice.service_report()
        elif service_action in ["--start", "--stop", "--restart"]:
            if len(sys.argv) < 4:
                print(f"Error: Service name is required for --service {service_action}")
                sys.exit(1)
            service_name = sys.argv[3]
            if service_action == "--start":
                checkservice.start_service(service_name)
            elif service_action == "--stop":
                checkservice.stop_service(service_name)
            elif service_action == "--restart":
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
            subprocess.run(["glances"])
            
        else:
            print("Invalid monitor action.")
            sys.exit(1)

    elif command in ["--help", "-H"]:
        manual.help()
        if len(sys.argv) > 2:
            help_command = sys.argv[2]
            if help_command in ["--scan", "-SS"]:
                manual.scan_help()
            elif help_command in ["--encrypt", "-E"]:
                manual.encrypt_help()
            elif help_command in ["--sort", "-S"]:
                manual.sort_help()
            elif help_command in ["--firewall", "-FW"]:
                manual.firewall_help()
            elif help_command == "--service":
                manual.service_help()
            elif help_command == "--port":
                manual.port_help()
            elif help_command in ["--all", "-A"]:
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

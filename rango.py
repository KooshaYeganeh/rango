#!/usr/bin/python3

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

def main():
    print(" ========== Rango is Simple DLP (Data Loss Prevention) For Linux Users ==========")
    print(" ========== Manual or Help : show Help ==========")

    if len(sys.argv) < 2:
        print("No command provided. Use --help or -H for usage information.")
        return

    command = sys.argv[1]

    if command in ("--encrypt", "-E"):
        if len(sys.argv) < 3:
            print("Directory path missing for encryption.")
            return
        directory_path = sys.argv[2]
        encrypt.encrypt_files_in_directory(directory_path, encrypt.get_key())
        print("All Files Encrypted [ OK ]")

    elif command in ("--sort", "-S"):
        if len(sys.argv) < 3:
            print("Directory path missing for sorting.")
            return
        directory_path = sys.argv[2]
        print(sort.sort_files(directory_path))

    elif command in ("--scan", "-SS"):
        if len(sys.argv) < 3:
            print("Scan option missing. Use --help or -H for usage information.")
            return

        scan_option = sys.argv[2]
        if scan_option in ("--full", "-F"):
            scan.full_clamav()
        elif scan_option in ("--dir", "-D"):
            scan.dir_clamav()
        elif scan_option in ("--rootkit", "-RK"):
            scan.rkhunter()
        elif scan_option in ("--vul", "-VUL"):
            scan.vul_check()
        else:
            print("Invalid scan option. Check manual for valid scan switches.")

    elif command in ("--firewall", "-FW"):
        if len(sys.argv) < 3:
            print("Firewall option missing. Use --help or -H for usage information.")
            return

        firewall_option = sys.argv[2]
        if firewall_option in ("--webserver", "-WB"):
            firewall.set_webserver_firewall()
        elif firewall_option in ("--check", "-C"):
            firewall.show_firewall_config()
        else:
            print("Invalid firewall option. Check manual for valid firewall switches.")

    elif command in ("--checkport", "-CP"):
        if len(sys.argv) < 3:
            print("Checkport option missing. Use --help or -H for usage information.")
            return

        checkport_option = sys.argv[2]
        if checkport_option in ("--result", "-R"):
            result = checkport.show_port()
            print(result)
        else:
            print("Invalid checkport option. Check manual for valid checkport switches.")

    elif command == "--service":
        if len(sys.argv) < 3:
            print("Service option missing. Use --help or -H for usage information.")
            return

        service_option = sys.argv[2]
        if service_option == "--list":
            checkservice.service()
        elif service_option == "--start":
            checkservice.start_service()
        elif service_option == "--stop":
            checkservice.stop_service()
        elif service_option == "--restart":
            checkservice.restart()
        else:
            print("Invalid service option. Check manual for valid service switches.")

    elif command == "--monitor":
        if len(sys.argv) < 3:
            print("Monitor option missing. Use --help or -H for usage information.")
            return

        monitor_option = sys.argv[2]
        if monitor_option == "--system":
            print("\n\nEnter command glances to Monitor system :)")
            print("➜ command : glances")

    elif command in ("--help", "-H"):
        manual.help()
        if len(sys.argv) < 3:
            return

        help_option = sys.argv[2]
        if help_option in ("--scan", "-SS"):
            manual.scan_help()
        elif help_option in ("--encrypt", "-E"):
            manual.encrypt_help()
        elif help_option in ("--sort", "-S"):
            manual.sort_help()
        elif help_option in ("--firewall", "-FW"):
            manual.firewall_help()
        elif help_option == "--service":
            manual.service_help()
        elif help_option == "--port":
            manual.port_help()
        elif help_option in ("--all", "-A"):
            manual.all()
        else:
            manual.help()

    else:
        print("Invalid command. Use --help or -H for usage information.")

if __name__ == "__main__":
    main()


import os
import sys


print(" ========== Rango is Simple DLP (Data Loss Prevention) For Linux Users ==========")
print(" ========== Manual or Help : show Help ==========")



def help():
    return("rango --help or -H")



def encrypt_help():
    print("\tEncrypt")
    print("rango --encrypt DIRECTORY or rango -E DIRECTORY")
    print("\tExample : ➜  rango --encrypt /tmp/Koosha")
    return " "


def sort_help():
    print("Sort : Sort Files in Given Directory")
    print("rango --sort DIRECTORY")
    print("\tExample : ➜  rango --sort /home/koosha/Desktop")
    return " "



def scan_help():
    print("\tScan")
    print("\tFull Scan : Full Scan of System with ClamAV and RKHunter and Lynis")
    print("\t\t➜  rango --scan --full")
    print("\t\t\trango -SS -F")
    print("\t\t➜  rango --scan --dir /home/koosha/Downloads")
    print("\t\t➜  rango -SS -D /home/koosha/Downloads")
    print("\t\t➜  rango --scan --rootkit")
    print("\t\t➜  rango -SS -RK")
    print("\t\t➜  rango --scan --vul")
    print("\t\t➜  rango -SS -VUL")
    return " "


def firewall_help():
    print("FireWall")
    print("\tWebServer : add Firewall configs For WebServer Automatically")
    print("\t\t➜  rango --firewall --webserver")
    print("\t\t➜  rango -FW -WB")
    print("\tcheck : check Firewall configs")
    print("\t\t➜  rango --firewal --check")
    print("\t\t➜  rango -FW -C")
    return " "


def all():
    print(firewall_help())
    print(scan_help())
    print(sort_help())
    print(encrypt_help())
    return " " 

# Rango

Data Loss Prevention (DLP) for Linux

![Rango](./static/python rango.py3.jpg)

## Overview

Rango is a modular Data Loss Prevention (DLP) tool designed for Linux systems, originally developed for use on SUSE operating systems. This tool provides functionalities for encryption, file sorting, system scanning, firewall configuration, port checking, and service management.

## Features

- **Encrypt Files**: Secure your files by encrypting them.
- **Sort Files**: Organize files by their extension.
- **Scan System**: Perform comprehensive security scans with ClamAV, RKHunter, and Lynis.
- **Manage Firewall**: Configure firewall rules and check existing configurations.
- **Check Ports**: Identify open ports on the system.
- **Manage Services**: List, start, stop, and restart system services.

## Commands and Options

### Encrypt

Encrypt files within a specified directory.


python rango.py --encrypt DIRECTORY
python rango.py -E DIRECTORY



**Example:**

```
python rango.py --encrypt /tmp/Koosha
```



### Sort

Sort files in a specified directory by their extensions.

python rango.py --sort DIRECTORY
python rango.py -S DIRECTORY


**Example:**

python rango.py --sort /home/$USER/Desktop


### Scan

Perform different types of scans on the system.

- **Full System Scan**: Use ClamAV, RKHunter, and Lynis for a complete system scan.




### Scan

Perform different types of scans on the system.

- **Full System Scan**: Use ClamAV, RKHunter, and Lynis for a complete system scan.


python rango.py --scan --full
python rango.py -SS -F



- **Directory Scan**: Scan a specific directory.

python rango.py --scan --dir /home/$USER/Downloads
python rango.py -SS -D /home/$USER/Downloads


- **RootKit Scan**: Check for rootkits.

python rango.py --scan --rootkit
python rango.py -SS -RK


- **Vulnerability Scan**: Identify system vulnerabilities.

python rango.py --scan --vul
python rango.py -SS -VUL



### Firewall

Manage firewall settings and check configurations.

- **WebServer Configuration**: Automatically add firewall rules for web servers.



python rango.py --firewall --webserver
python rango.py -FW -WB



- **Check Firewall Configurations**: Review existing firewall rules.


python rango.py --firewall --check
python rango.py -FW -C




### Port Scanning

Check for open ports on the system.

python rango.py --checkport --result
python rango.py -CP -R




### Service Management

Manage system services: list, start, stop, and restart services.

- **List Services**:



python rango.py --service --list



- **Start Service**:

python rango.py --service --start SERVICE_NAME



- **Stop Service**:

python rango.py --service --stop SERVICE_NAME


- **Restart Service**:

python rango.py --service --restart SERVICE_NAME



## Installation

To install Rango, run the following commands:

```bash
wget https://github.com/KooshaYeganeh/python rango.py/archive/refs/heads/main.zip
unzip main.zip
echo "1- Main file unzipped"
mv python rango.py-main python rango.py
mv python rango.py /opt
echo "2- Main directory moved to /opt"
cd /usr/bin
sudo ln -s /opt/python rango.py/python rango.py ./python rango.py
echo "3- Created symbolic link in /usr/bin"
echo "4- Rango DLP installed successfully [ OK ]"
```

## Manual
Help
Display help and usage information.



python rango.py --help
python rango.py -H


python rango.py --encrypt DIRECTORY
python rango.py -E DIRECTORY


python rango.py --sort DIRECTORY
python rango.py -S DIRECTORY

python rango.py --scan --full
python rango.py -SS -F

python rango.py --scan --dir /home/$USER/Downloads
python rango.py -SS -D /home/$USER/Downloads


python rango.py --scan --rootkit
python rango.py -SS -RK


python rango.py --scan --vul
python rango.py -SS -VUL

python rango.py --firewall --webserver
python rango.py -FW -WB


python rango.py --firewall --check
python rango.py -FW -C


python rango.py --checkport --result
python rango.py -CP -R


python rango.py --service --list


python rango.py --service --start SERVICE_NAME


python rango.py --service --stop SERVICE_NAME


python rango.py --service --restart SERVICE_NAME








# Rango

Data Loss Prevention (DLP) for Linux

![Rango](./static/python_rango.py3.jpg)

## Overview

Rango is a modular Data Loss Prevention (DLP) tool designed for Linux systems, originally developed for use on SUSE operating systems. This tool provides functionalities for encryption, file sorting, system scanning, firewall configuration, port checking, and service management.

## Features

- 🔒 **Encrypt Files**: Secure your files by encrypting them.
- 📁 **Sort Files**: Organize files by their extension.
- 🛡️ **Scan System**: Perform comprehensive security scans with ClamAV, RKHunter, and Lynis.
- 🔥 **Manage Firewall**: Configure firewall rules and check existing configurations.
- 🌐 **Check Ports**: Identify open ports on the system.
- ⚙️ **Manage Services**: List, start, stop, and restart system services.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Commands and Options](#commands-and-options)
  - [Encrypt](#encrypt)
  - [Sort](#sort)
  - [Scan](#scan)
  - [Firewall](#firewall)
  - [Port Scanning](#port-scanning)
  - [Service Management](#service-management)
- [Installation](#installation)
- [Manual](#manual)
  - [Help](#help)
  - [Common Commands](#common-commands)

## Commands and Options

### Encrypt

Encrypt files within a specified directory.

```bash
python rango.py --encrypt DIRECTORY
python rango.py -E DIRECTORY
```

**Example:**

```bash
python rango.py --encrypt /tmp/Koosha
```

### Sort

Sort files in a specified directory by their extensions.

```bash
python rango.py --sort DIRECTORY
python rango.py -S DIRECTORY
```

**Example:**

```bash
python rango.py --sort /home/$USER/Desktop
```

### Scan

Perform different types of scans on the system.

- **Full System Scan**: Use ClamAV, RKHunter, and Lynis for a complete system scan.

```bash
python rango.py --scan --full
python rango.py -SS -F
```

- **Directory Scan**: Scan a specific directory.

```bash
python rango.py --scan --dir /home/$USER/Downloads
python rango.py -SS -D /home/$USER/Downloads
```

- **RootKit Scan**: Check for rootkits.

```bash
python rango.py --scan --rootkit
python rango.py -SS -RK
```

- **Vulnerability Scan**: Identify system vulnerabilities.

```bash
python rango.py --scan --vul
python rango.py -SS -VUL
```

### Firewall

Manage firewall settings and check configurations.

- **WebServer Configuration**: Automatically add firewall rules for web servers.

```bash
python rango.py --firewall --webserver
python rango.py -FW -WB
```

- **Check Firewall Configurations**: Review existing firewall rules.

```bash
python rango.py --firewall --check
python rango.py -FW -C
```

### Port Scanning

Check for open ports on the system.

```bash
python rango.py --checkport --result
python rango.py -CP -R
```

### Service Management

Manage system services: list, start, stop, and restart services.

- **List Services**:

```bash
python rango.py --service --list
```

- **Start Service**:

```bash
python rango.py --service --start SERVICE_NAME
```

- **Stop Service**:

```bash
python rango.py --service --stop SERVICE_NAME
```

- **Restart Service**:

```bash
python rango.py --service --restart SERVICE_NAME
```

## Installation

To install Rango, run the following commands:

```bash
./install --suse --app
./install --redhat --app
./install --debian --app
```

For Install Just Basic Tools : 

```bash
./install --suse 
./install --redhat 
./install --debian 
```

## Manual

### Help

Display help and usage information.

```bash
python rango.py --help
python rango.py -H
```

### Common Commands

```bash
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

python rango.py --firewall --show
python rango.py --add 'RULE'

python rango.py --checkport --result
python rango.py -CP -R

python rango.py --service --list

python rango.py --service --start SERVICE_NAME

python rango.py --service --stop SERVICE_NAME

python rango.py --service --restart SERVICE_NAME
```



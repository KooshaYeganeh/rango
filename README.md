# Rango

Data Loss Prevention (DLP) for Linux

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1280px-Tux.svg.png" alt="Linux Logo" width="200"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/83/The_GNU_logo.png" alt="GNU Logo" width="200"/>
<img src="https://static.fsf.org/common/img/logo-new.png" alt="Free Software Logo" width="200" height="60"/>
<img src="https://www.openmaint.org/images/opensource-logo.png/@@images/image.png" alt="openSOURCE" width="200"/>
<img src="https://en.opensuse.org/images/f/f2/Button-laptop-colour.png" alt="openSUSE Logo" width="200"/>
<img src="https://sfconservancy.org/static/img/conservancy-header.8c88caa4010b.svg" alt="Software Freedom Conservancy" width="200" height="100"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/Free_Software_Foundation_Europe%2C_logo.svg" alt="Software Freedom Conservancy" width="200" height="100"/><br/>


## DLP

DLP (Data Loss Prevention) software should have a range of features to effectively protect sensitive data from unauthorized access, use, or transmission. Here are some key features to look for:

1. **Data Discovery and Classification:**
   - **Content Inspection:** Ability to scan and classify data based on its content (e.g., credit card numbers, personal identification numbers).
   - **Contextual Analysis:** Understanding the context in which data is used to determine its sensitivity.

2. **Policy Management:**
   - **Customizable Policies:** Ability to create and enforce policies tailored to specific organizational needs and compliance requirements.
   - **Policy Templates:** Predefined templates for common regulations and industry standards (e.g., GDPR, HIPAA).

3. **Monitoring and Alerting:**
   - **Real-Time Monitoring:** Continuous surveillance of data flows and user activities to detect potential breaches or policy violations.
   - **Alerts and Notifications:** Immediate notifications of suspicious activities or policy violations to relevant stakeholders.

4. **Data Protection and Encryption:**
   - **Data Encryption:** Support for encrypting sensitive data both at rest and in transit to prevent unauthorized access.
   - **Data Masking:** Ability to obscure or mask sensitive information in non-production environments.

5. **Endpoint Protection:**
   - **Device Control:** Ability to manage and secure endpoints (e.g., USB drives, mobile devices) that interact with sensitive data.
   - **Application Control:** Restrictions on which applications can access or transmit sensitive data.

6. **Integration and Compatibility:**
   - **System Integration:** Compatibility with existing security infrastructure and IT systems (e.g., SIEM, firewalls, email systems).
   - **Cloud and On-Premises Support:** Protection for both cloud-based and on-premises environments.

7. **Incident Response:**
   - **Automated Response:** Automated actions in response to detected policy violations (e.g., blocking access, quarantining data).
   - **Incident Management:** Tools for investigating and managing security incidents, including detailed logs and reports.

8. **Reporting and Analytics:**
   - **Detailed Reports:** Comprehensive reporting on data protection status, policy violations, and compliance metrics.
   - **Analytics:** Advanced analytics to identify trends, assess risk, and improve data protection strategies.

9. **User and Role Management:**
   - **Access Controls:** Fine-grained access controls to ensure only authorized users can access sensitive data.
   - **User Behavior Analysis:** Monitoring user behavior to detect anomalies or risky actions.

10. **Compliance and Audit Support:**
    - **Regulatory Compliance:** Features to support compliance with various regulations and standards (e.g., GDPR, CCPA).
    - **Audit Trails:** Detailed logs of data access and policy enforcement for auditing and forensic purposes.

11. **Scalability and Performance:**
    - **Scalability:** Ability to scale with organizational growth and handle increasing volumes of data.
    - **Performance:** Efficient performance with minimal impact on system and network operations.


## Rango Overview

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



### **Command List**

1. **Encrypt Files**
   - `--encrypt DIRECTORY` or `-E DIRECTORY`
   - **Description**: Encrypt files in the specified directory.
   - **Example**: `python rango.py --encrypt /tmp/Koosha`

2. **Sort Files**
   - `--sort DIRECTORY` or `-S DIRECTORY`
   - **Description**: Sort files in the specified directory.
   - **Example**: `python rango.py --sort /home/koosha/Desktop`

3. **Scan Options**
   - **Full System Scan**
     - `--scan --full` or `-SS -F`
     - **Description**: Perform a full system scan with ClamAV, RKHunter, and Lynis.
     - **Example**: `python rango.py --scan --full`
   
   - **Directory Scan**
     - `--scan --dir DIRECTORY` or `-SS -D DIRECTORY`
     - **Description**: Perform a scan on the specified directory.
     - **Example**: `python rango.py --scan --dir /home/koosha/Downloads`
   
   - **Rootkit Scan**
     - `--scan --rootkit` or `-SS -RK`
     - **Description**: Perform a rootkit scan using RKHunter.
     - **Example**: `python rango.py --scan --rootkit`
   
   - **Vulnerability Scan**
     - `--scan --vul` or `-SS -VUL`
     - **Description**: Perform a general vulnerability scan.
     - **Example**: `python rango.py --scan --vul`
   
   - **Vulnerability Scan with Fail2Ban**
     - `--scan --vul --fail2ban` or `-SS -VUL -FB`
     - **Description**: Perform a vulnerability scan and check Fail2Ban logs.
     - **Example**: `python rango.py --scan --vul --fail2ban`

4. **Firewall Options**
   - **Set WebServer Firewall**
     - `--firewall --webserver` or `-FW -WB`
     - **Description**: Configure firewall rules for a web server.
     - **Example**: `python rango.py --firewall --webserver`
   
   - **Show Firewall Configurations**
     - `--firewall --show` or `-FW -SH`
     - **Description**: Display current firewall configurations.
     - **Example**: `python rango.py --firewall --show`
   
   - **Add Firewall Rule**
     - `--firewall --add 'RULE'` or `-FW -A 'RULE'`
     - **Description**: Add a specific firewall rule.
     - **Example**: `python rango.py --firewall --add 'RULE'`

5. **Check Open Ports**
   - `--checkport --result` or `-CP -R`
   - **Description**: Check for open ports on the system.
   - **Example**: `python rango.py --checkport --result`

6. **Service Options**
   - **List Services**
     - `--service --list`
     - **Description**: List all services.
     - **Example**: `python rango.py --service --list`
   
   - **Service Report**
     - `--service --report`
     - **Description**: Generate a report on services.
     - **Example**: `python rango.py --service --report`
   
   - **Start a Service**
     - `--service start SERVICE_NAME`
     - **Description**: Start the specified service.
     - **Example**: `python rango.py --service start nginx`
   
   - **Stop a Service**
     - `--service stop SERVICE_NAME`
     - **Description**: Stop the specified service.
     - **Example**: `python rango.py --service stop nginx`
   
   - **Restart a Service**
     - `--service restart SERVICE_NAME`
     - **Description**: Restart the specified service.
     - **Example**: `python rango.py --service restart nginx`

7. **Monitor Options**
   - `--monitor --system`
   - **Description**: Display a command to monitor the system using `glances`.
   - **Example**: `python rango.py --monitor --system`

8. **Help**
   - `--help` or `-H`
   - **Description**: Display the general help message.
   - **Example**: `python rango.py --help`
   
   - **Detailed Help**
     - `--help COMMAND` or `-H COMMAND`
     - **Description**: Display detailed help for a specific command.
     - **Example**: `python rango.py --help --scan` or `python rango.py -H --scan`


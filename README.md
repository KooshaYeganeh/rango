# Rango

Data Loss Prevention For Linux

![Rango](./static/rango3.jpg)


## INFO

This software is a modular DLP (Data Loss Prevention) for Linux, which was designed based on personal needs on the Suse operating system, that's why I chose this logo for the software:)



## Manual

----------------------------------------------------------
----------------------------------------------------------

### Encrypt

*rango --encrypt DIRECTORY or rango -E DIRECTORY*


```
rango --encrypt /tmp/Koosha
```

----------------------------------------------------------
----------------------------------------------------------

### Sort

**Sort Files in Given Directory**

*rango --sort DIRECTORY*

```
rango --sort /home/$USER/Desktop
```

----------------------------------------------------------
----------------------------------------------------------

### Scan

*Full Scan : Full Scan of System with ClamAV and RKHunter and Lynis*

---------------------------------------------------------
```
rango --scan --full
```
**or**

```
rango -SS -F
```
----------------------------------------------------------
*Directory Scan : Scan Given Directory*

```
rango --scan --dir /home/$USER/Downloads
```
**or**

```
rango -SS -D /home/$USER/Downloads
```
----------------------------------------------------------

*Scan RootKit*

```
rango --scan --rootkit
```
**or**
```
rango -SS -RK
```
```
rango --scan --vul
```

```
rango -SS -VUL
```

----------------------------------------------------------
----------------------------------------------------------

### FireWall

**WebServer :** add Firewall configs For WebServer Automatically

```
rango --firewall --webserver
```
or

```
rango -FW -WB
```

*check : check Firewall configs*

```
rango --firewal --check
```

```
rango -FW -C
```

 

----------------------------------------------------------
----------------------------------------------------------

### Port Scaning

show openports : 

```
rango --checkport --result
```
or

```
rango -CP -R
```

----------------------------------------------------------
----------------------------------------------------------

### Service

list services : 

```
rango --service --list
```

start service

```
rango --service --start SERVICE_NAME
```


stop service

```
rango --service --stop SERVICE_NAME
```


restart service

```
rango --service --restart SERVICE_NAME
```




## Install

```
wget https://github.com/KooshaYeganeh/rango/archive/refs/heads/main.zip && unzip main.zip && echo "1- Main File unziped"  && mv rango-main rango && mv rango /opt && echo "2- Main Directory Moved to /opt " && cd /usr/bin && sudo ln -s /opt/rango/rango ./rango && echo "3- Created SoftLink From MainFile in /usr/bin" && echo "4- Rango DLP Installed Successfully [ OK ]"
```


## Remove


```
sudo rm -rf /opt/rango && echo "1- Main Directort Removed" && sudo rm /usr/bin/rango && echo "Rango DLP Removed [ OK ]"
```


## Other Tools


### Install Zeek

#### Fedora 37

```
sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/security:zeek/Fedora_37/security:zeek.repo && sudo dnf install zeek -y
```

#### Fedora38


```
sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/security:zeek/Fedora_38/security:zeek.repo && sudo dnf install zeek

```

```
export PATH=$PATH:/opt/zeek/bin
```

### openSUSE 15.5

```
sudo zypper addrepo https://download.opensuse.org/repositories/security:zeek/15.5/security:zeek.repo
zypper refresh
sudo zypper install zeek -y
```


### UBuntu

```
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list && curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null && sudo apt update && sudo apt install zeek-6.0
```




### Zeek Manual



**1- Navigate to Zeek Configuration Directory:**


```
cd /opt/zeek/etc
```

**2- Copy the Default Configuration:**

Copy the Default Configuration:


**3- Edit local.zeek:**
```
sudo cp zeekctl.cfg local.zeek
```

> Edit local.zeek:


```
sudo vi local.zeek
```


**- Enable/Disable Protocols:**

> Uncomment or comment out lines to enable or disable specific analyzers. For example, to enable HTTP and DNS analysis:

```
@load protocols/http
@load protocols/dns
```

**- File Analysis Configuration:**

Configure settings related to file analysis, such as enabling extraction of files. Uncomment or add lines like:

```
@load frameworks/files/extract-all-files
```

**- Logging Configuration:**

Configure the log settings, including the log directory and log rotation policy. For example:

```
Log::default_rotation_interval = 1 day;
Log::default_rotation_base_count = 2;
```

**- Capture Interfaces:**

Specify the network interfaces to monitor. For example:

```
interface="eth0"
```

Save the changes.


**4 - Restart Zeek:**

> After making changes to the local.zeek file, restart Zeek to apply the new configuration:

```
zeekctl stop && zeekctl deploy && zeekctl start
```

> The zeekctl deploy command updates the configuration across the Zeek cluster.


**5- Review Logs:**
Zeek generates various log files in the logs directory. You can review these logs to verify that Zeek is capturing and analyzing network traffic according to your configuration.





























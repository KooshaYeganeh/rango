# Rango

Data Loss Prevention For Linux

![Rango](./static/rango3.jpg)


## INFO

This software is a modular DLP (Data Loss Prevention) for Linux, which was designed based on personal needs on the Suse operating system, that's why I chose this logo for the software:)



## Manual

### Encrypt

*rango --encrypt DIRECTORY or rango -E DIRECTORY*


```
rango --encrypt /tmp/Koosha
```

### Sort

**Sort Files in Given Directory**

*rango --sort DIRECTORY*

```
rango --sort /home/$USER/Desktop
```


### Scan

*Full Scan : Full Scan of System with ClamAV and RKHunter and Lynis*

```
rango --scan --full
```
```
rango -SS -F
```
```
rango --scan --dir /home/$USER/Downloads
```


```
rango -SS -D /home/$USER/Downloads
```

```
rango --scan --rootkit
```
```
rango -SS -RK
```
```
rango --scan --vul
```

```
rango -SS -VUL
```

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

 



## Install

```
wget https://github.com/KooshaYeganeh/rango/archive/refs/heads/main.zip && unzip main.zip && echo "1- Main File unziped"  && mv rango-main rango && mv rango /opt && echo "2- Main Directory Moved to /opt " && cd /usr/bin && sudo ln -s /opt/rango/rango ./rango && echo "3- Created SoftLink From MainFile in /usr/bin" && echo "4- Rango DLP Installed Successfully [ OK ]"
```


## Remove


```
sudo rm -rf /opt/rango && echo "1- Main Directort Removed" && sudo rm /usr/bin/rango && echo "Rango DLP Removed [ OK ]"
```


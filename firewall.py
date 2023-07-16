import os
import sys




def show_firewall_config():
    show = os.popen("sudo iptables -nvL --line-numbers").read()
    print(show)
    return "Current Firewall Configs [ OK ] "



def set_webserver_firewall():
    com1 = os.popen("sudo iptables -A INPUT -i enp1s0 -p tcp -m multiport ! --dport 22,80,443 -j REJECT").read()

    com2 = os.popen("udo iptables -A INPUT -i enp1s0 -p tcp ! --syn -m state --state NEW -j DROP").read()
    com3 = os.popen("sudo iptables -A INPUT -i enp1s0 -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT").read()
    com4 = os.popen("sudo iptables -A OUTPUT -o enp1s0 -p tcp -m multiport --sport 22,80,443 -j ACCEPT").read()
    com5 = os.popen("udo iptables -A INPUT -i enp1s0 -p tcp --tcp-flags ALL NONE -j DROP").read()
    com6 = os.popen("sudo iptables -A INPUT -i enp1s0 -p tcp --tcp-flags PSH,URG,FIN PSH,URG,FIN -j REJECT").read()
    com7 = os.popen("sudo iptables -A INPUT -p tcp -m state --state INVALID -j DROP").read()
    com8 = os.popen("sudo iptables -A INPUT -p tcp -m connlimit --connlimit-above 100 -j DROP").read()
    com9 = os.popen("sudo iptables -A INPUT -f -j DROP").read()
    com10 = os.popen("sudo iptables -A INPUT -p icmp --icmp-type 8 -j DROP").read()
    com11 = os.popen("udo iptables -A INPUT -p icmp --icmp-type 13 -j DROP").read()
    com12 = os.popen("udo iptables -A INPUT -p icmp --icmp-type 14 -j DROP").read()
    com13 = os.popen("sudo iptables -A INPUT -i enp1s0 -p tcp --syn -m limit --limit 100/minute --limit-burst 80 -j DROP").read()
    
    com14 = os.popen("sudp iptables -P INPUT DROP").read()

    com15 = os.popen("sudo iptables -p OUTPUT DROP").read()
    print(com,com1,com2,com3,com4,com5,com6,com7,com8,com9,com10,com11,com12,com13)
    return "WebServer Firewall Configs [ OK ]"


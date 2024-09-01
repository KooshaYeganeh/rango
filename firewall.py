import os
import sys
import argparse

def show_firewall_config():
    show = os.popen("sudo iptables -nvL --line-numbers").read()
    print(show)
    return "Current Firewall Configs [ OK ] "

def set_webserver_firewall():
    commands = [
        "sudo iptables -A INPUT -i enp1s0 -p tcp -m multiport ! --dport 22,80,443 -j REJECT",
        "sudo iptables -A INPUT -i enp1s0 -p tcp ! --syn -m state --state NEW -j DROP",
        "sudo iptables -A INPUT -i enp1s0 -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT",
        "sudo iptables -A OUTPUT -o enp1s0 -p tcp -m multiport --sport 22,80,443 -j ACCEPT",
        "sudo iptables -A INPUT -i enp1s0 -p tcp --tcp-flags ALL NONE -j DROP",
        "sudo iptables -A INPUT -i enp1s0 -p tcp --tcp-flags PSH,URG,FIN PSH,URG,FIN -j REJECT",
        "sudo iptables -A INPUT -p tcp -m state --state INVALID -j DROP",
        "sudo iptables -A INPUT -p tcp -m connlimit --connlimit-above 100 -j DROP",
        "sudo iptables -A INPUT -f -j DROP",
        "sudo iptables -A INPUT -p icmp --icmp-type 8 -j DROP",
        "sudo iptables -A INPUT -p icmp --icmp-type 13 -j DROP",
        "sudo iptables -A INPUT -p icmp --icmp-type 14 -j DROP",
        "sudo iptables -A INPUT -i enp1s0 -p tcp --syn -m limit --limit 100/minute --limit-burst 80 -j DROP",
        "sudo iptables -P INPUT DROP",
        "sudo iptables -P OUTPUT DROP"
    ]
    
    for command in commands:
        result = os.popen(command).read()
        print(result)

    return "WebServer Firewall Configs [ OK ]"

def add_rule(rule):
    chain, *rule_params = rule.split()
    command = f"sudo iptables -A {chain} {' '.join(rule_params)}"
    print(f"Executing command: {command}")
    
    result = os.popen(command).read()
    print(result)
    
    return f"Rule added to {chain} [ OK ]"

def main():
    parser = argparse.ArgumentParser(description="Manage firewall rules.")
    parser.add_argument("--firewall", action="store_true", help="Manage firewall rules")
    parser.add_argument("--show", action="store_true", help="Show current firewall configuration")
    parser.add_argument("--set", action="store_true", help="Set webserver firewall rules")
    parser.add_argument("--add", type=str, help="Add a new iptables rule")

    args = parser.parse_args()

    if args.firewall:
        if args.show:
            print(show_firewall_config())
        elif args.set:
            print(set_webserver_firewall())
        elif args.add:
            print(add_rule(args.add))
        else:
            print("No action specified. Use --show, --set, or --add.")
            sys.exit(1)
    else:
        print("Please specify --firewall to manage firewall rules.")
        sys.exit(1)

if __name__ == "__main__":
    main()

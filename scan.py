import os
import sys
import subprocess



def dir_clamav():
    scan = os.popen("sudo clamscan --remove --recursive --infected {scan_path}").read()
    print(scan)
    return "clamav Scaneed Directory [ OK ]"



def rkhunter():
    scan = os.popen("sudo rkhunter --check").read()
    result = subprocess.run(['rkhunter', '--check'], capture_output=True, text=True)
    print("start Scan system with RootKitHunter")
    print(result.stdout)

    if result.returncode == 0:
        return "system Scanned with RootKitHunter [ OK ]"
    else:
        return "RootKit Scan System [ ERROR ]"



def vul_check():
    vul = os.popen("sudo lynis audit system").read()
    print(vul)
    return "sysem Vulnerability check Done with ciscofy Lynis [ OK ]"


def full_clamav():
    clamascan = os.popen("sudo clamscan --remove --infected --recursive /").read()
    rkhunter = os.popen("sudo rkhunter -c").read()

    print(clamscan)
    print(rkhunter)
    print(vul_check())
    return "Scanned Full system [ OK ]"




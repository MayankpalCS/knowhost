import sys
import ipaddress
from scapy.all import srp
from scapy.layers.l2 import ARP
from scapy.layers.l2 import ARP ,Ether
from colorama import init, Fore
def banner():
    print("""%s
            |  / ||   | |------| |     | |    | |----| --------- ---------
            | /  | |  | |      | |     | |    | |    | |             |  
            |/   |  | | |      | |  |  | |----| |    | |-------|     | 
            ||   |   || |      | | | | | |    | |    |         |     |
            | |  |    | |------| ||   || |    | |----| --------|     |
            @ developed by mayank
                           """)
banner()
target=sys.argv[1]
init()
red=Fore.RED
green=Fore.GREEN
#a list to sstore hosts
print("demo:python3 arpfinder.py 192.168.159.0/24")
online_host=[]
#ff:ff:ff:ff:ff:ff is broadcast adress
ether=Ether(dst="ff:ff:ff:ff:ff:ff")
arp=ARP(pdst=target)
#enscapsulating ip and arp packets
packet=ether/arp

#setting timeout 
result=srp(packet, timeout=4)
uphost = result[0]
for sent, received in uphost:
    online_host.append({'ip': received.psrc, 'mac': received.hwsrc})
print(f"{green}uphosts:")
print("IP\t\t\t\t\tMAC")
for host in online_host:
    print("[+]{}\t\t{}".format(host['ip'], host['mac']))

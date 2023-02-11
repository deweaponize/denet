#!/usr/bin/env python3

import scapy.all as scapy
import sys
import time
def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast,timeout=3,verbose=0)[0]
    clients= []
    for sent, received in answered_list:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    try:
        return clients[0]['mac']
    except IndexError:
        pass
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    time.sleep(int(sys.argv[2]))
    print(packet.show())

sniff(sys.argv[1])                                                                                                                     

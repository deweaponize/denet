#!/usr/bin/env python3

import scapy.all as scapy
import sys

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
    if packet.haslayer(scapy.ARP):
        # print(packet.show())
        # print("hi")
        # print(get_mac(packet[scapy.ARP].pdst))
        real_mac = get_mac(packet[scapy.ARP].psrc)
        # print(real_mac)
        response_mac = packet[scapy.ARP].hwsrc

        if real_mac != response_mac:
            print("[+] You are under attack!!")
        else:
            pass

sniff(sys.argv[1])                                                                                                                     

#!/usr/bin/env python3

import scapy.all as scapy
import subprocess as sub
import re

def getip():
    process =sub.Popen(['ip', 'a'], stdout=sub.PIPE, stderr=sub.PIPE)
    stdout, stderr = process.communicate()
    ipre = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d\d)')
    match = re.findall(ipre,str(stdout))
    return match

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=3,verbose=0)[0]
    clients=[]
    for sent, received in answered_list:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))


ipOfSystem = getip()
# print(ipOfSystem[0])
# scan(ipOfSystem[0])
# print(ipOfSystem)
scan(ipOfSystem[0])
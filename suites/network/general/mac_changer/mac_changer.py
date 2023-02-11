#!/usr/bin/env python3
import subprocess as sub
import sys
import re

print("RUN THIS FILE AS ADMINISTRATOR!!")
def change_mac(interface, new_mac):
  if len(new_mac) != 17:
    print('[*] Please enter a valid MAC Address')
    quit()
  print('[+] Changing the MAC Address to', new_mac)
  sub.call(['ifconfig', interface, 'down'])
  sub.call(['ifconfig', interface, 'hw', 'ether', new_mac])
  sub.call(['ifconfig', interface, 'up'])
  
def get_current_mac(interface):
  output = sub.check_output(['ifconfig', interface], universal_newlines = True)
  search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
  if search_mac:
    return search_mac.group(0)
  else:
    print('[*] Could not read the MAC Address')
    
interf= sys.argv[1]
newmacad = sys.argv[2]
interface_mac= get_current_mac(interface=interf)
change_mac(interface=interf,new_mac=newmacad)

print(f"Succesfuly changed mac address {interface_mac} to {newmacad}")

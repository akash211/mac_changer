#!/usr/bin/env python3


import subprocess

interface = input("interface > ")
new_mac = input("new mac > ")

print("[+] Changing mac_address of " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig", interface])

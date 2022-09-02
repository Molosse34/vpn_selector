#!/usr/bin/python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--vpn", type=str, default="Default value", help="to choose the vpn")
args = parser.parse_args()



if args.vpn == "htb":
	os.system('gnome-terminal -- bash -c "openvpn /usr/share/vpn/htb_vpn.ovpn"')
if args.vpn == "thm":
	os.system('gnome-terminal -- bash -c "openvpn /usr/share/vpn/thm_vpn.ovpn"')

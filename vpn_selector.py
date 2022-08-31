#!/usr/bin/python3

import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('thm',help="start the vpn for thm in a new ternminal", )
parser.add_argument('htb',help="start the vpn for htb in a new ternminal", )
args = parser.parse_args()

if args.htb:
	os.system('gnome-terminal -- bash -c "openvpn /usr/share/vpn/htb_vpn.ovpn"')
if args.thm:
	os.system('gnome-terminal -- bash -c "openvpn /usr/share/vpn/thm_vpn.ovpn"')
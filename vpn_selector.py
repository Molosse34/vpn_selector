#!/usr/bin/python3

import os
import argparse
import json 

parser = argparse.ArgumentParser()
parser.add_argument( '-v',"--vpn", type=str, default="Default value", help="to choose the vpn")
parser.add_argument("-c","--change", help="change the variable", action='store_true')
args= parser.parse_args()


if not os.path.exists('chemin_vpn_htb.json'):
    with open('chemin_vpn_htb.json', 'w') as file:
        json.dump({}, file)

if not os.path.exists('chemin_vpn_thm.json'):
    with open('chemin_vpn_thm.json', 'w') as file:
        json.dump({}, file)


with open('chemin_vpn_htb.json', 'r') as file:
		a = json.load(file)
with open('chemin_vpn_thm.json', 'r') as file:
		b = json.load(file)


if args.change == True:
	a = input('écrit le chemain du vpn htb: ')
	b = input('écrit le chemain du vpn thm: ')

	with open('chemin_vpn_htb.json', 'w') as file:
            json.dump(a, file)
	with open('chemin_vpn_thm.json', 'w') as file:
            json.dump(b, file)





if args.vpn == "htb":
	try:
	os.system(f'bash -c "openvpn {a}"')
	except SyntaxError:
		print("wrong path")

elif args.vpn == "thm":
	try:
	os.system(f'bash -c "openvpn {b}"')
	except SyntaxError:
		print('wrong path')

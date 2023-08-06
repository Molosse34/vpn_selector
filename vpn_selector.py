#!/usr/bin/python3

import os
import argparse
import json 
import pathlib
import readline


def complete_path(text, state):
    incomplete_path = pathlib.Path(text)
    if incomplete_path.is_dir():
        completions = [p.as_posix() for p in incomplete_path.iterdir()]
    elif incomplete_path.exists():
        completions = [incomplete_path]
    else:
        exists_parts = pathlib.Path('.')
        for part in incomplete_path.parts:
            test_next_part = exists_parts / part
            if test_next_part.exists():
                exists_parts = test_next_part

        completions = []
        for p in exists_parts.iterdir():
            p_str = p.as_posix()
            if p_str.startswith(text):
                completions.append(p_str)
    return completions[state]

parser = argparse.ArgumentParser()
parser.add_argument( '-v',"--vpn", type=str, default="Default value", help="to choose the vpn")
parser.add_argument("-c","--change", help="change the variable", action='store_true')
args= parser.parse_args()




if not os.path.exists('/opt/vpn_selector/chemin_vpn_htb.json'):
    with open('/opt/vpn_selector/chemin_vpn_htb.json', 'w') as file:
        json.dump({}, file)

if not os.path.exists('/opt/vpn_selector/chemin_vpn_thm.json'):
    with open('/otp/vpn_selctor/chemin_vpn_thm.json', 'w') as file:
        json.dump({}, file)


with open('/opt/vpn_selector/chemin_vpn_htb.json', 'r') as file:
		a = json.load(file)
with open('/opt/vpn_selector/chemin_vpn_thm.json', 'r') as file:
		b = json.load(file)


if args.change == True:
	readline.set_completer_delims(' \t\n;')
	readline.parse_and_bind("tab: complete")
	readline.set_completer(complete_path)
	
	a = input('écrit le chemin du vpn htb: ')
	b = input('écrit le chemin du vpn thm: ')

	with open('/opt/vpn_selector/chemin_vpn_htb.json', 'w') as file:
            json.dump(a, file)
	with open('/opt/vpn_selector/chemin_vpn_thm.json', 'w') as file:
            json.dump(b, file)





if args.vpn == "htb":
	try:
		os.system(f'gnome-terminal -- bash -c "openvpn {a}"')
	except SyntaxError:
		print("wrong path")

elif args.vpn == "thm":
	try:
		os.system(f'gnome-terminal -- bash -c "openvpn {b}"')
	except SyntaxError:
		print('wrong path')

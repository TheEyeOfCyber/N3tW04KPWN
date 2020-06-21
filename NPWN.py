import argparse
import modules.data
import modules.resolve
import modules.curl
from modules import *
import sys


def banner():
    print(""" \033[1;34m
             ('-. .-.               .-')    .-') _            ('-.                 ('-.
            ( OO )  /     Ghost    ( OO ). (  OO) )         _(  OO)      Eye     _(  OO)
  ,----.    ,--. ,--. .-'),-----. (_)---\_)/     '._       (,------. ,--.   ,--.(,------.
 '  .-./-') |  | |  |( OO'  .-.  '/    _ | |'--...__)       |  .---'  \  `.'  /  |  .---'
 |  |_( O- )|   .|  |/   |  | |  |\  :` `. '--.  .--'       |  |    .-')     /)  |  |
 |  | .--, \|       |\_) |  |\|  | '..`''.)   |  |         (|  '--.(OO  \   /.  (|  '--.
(|  | '. (_/|  .-.  |  \ |  | |  |.-._)   \   |  |          |  .--' |   /  /     |  .--'
 |  '--'  | |  | |  |   `'  '-'  '\       /   |  |          |  `---.`-./  /      |  `---.
  `------'  `--' `--'     `-----'  `-----'    `--'          `------'  `--'       `------'
            \033[1;m


def main():
    banner()
    parser = argparse.ArgumentParser(description='Python Network Tools')
    parser.add_argument('--ucurl', action='store_true', help='Curl a provided URL with urllib must use http://')
    parser.add_argument('--mx', action='store_true', help='Lookup MX record')
    parser.add_argument('--dnsresolve', action='store_true', help='resolve hostname')
    parser.add_argument('--dnsreverse', action='store_true', help='reverse lookup')
    parser.add_argument('--targets', required=True, help='file to open')
    args = parser.parse_args()

    if args.ucurl:
        host_list = data.make_list_file(args.targets)
        curl.urllib_curl(host_list)
    if args.mx:
        host_list = data.make_list_file(args.targets)
        resolve.mx_lookup(host_list)
    if args.dnsresolve:
        host_list = data.make_list_file(args.targets)
        resolve.resolve_hostname(host_list)
    if args.dnsreverse:
        ip_list = data.make_list_file(args.targets)
        resolve.reverse_lookup(ip_list)

if __name__ == "__main__":
    main()

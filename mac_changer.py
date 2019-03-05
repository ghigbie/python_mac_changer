#!/usr.bin.env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", '--interface', dest="interface", help="Interface to change its MAC aaddress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, user --help for more info.")
    return options


def mac_changer(interface, change_to):
    print(f'Changing MAC address for {interface} to {change_to}')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', change_to])
    subprocess.call(['ifconfig', interface, 'up'])
    print('Interface changed')
    subprocess.call("ifconfig", shell=True)


options = get_arguments()
# mac_changer(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print("IFCONFIG RESULT: ")
print(ifconfig_result)
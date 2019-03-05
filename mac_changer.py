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

ifconfig_result = str(subprocess.check_output(["ifconfig", options.interface]))
print("IFCONFIG RESULT: ")
print(type(ifconfig_result))

mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
if mac_address_search_result:
    print("MAC ADDRESS SEARCH RESULT: ", mac_address_search_result.group(0))
else:
    print("[-] Could not find MAC address : (")


def mac_match(retreived_mac, new_mac_address):
    if retreived_mac == new_mac_address:
        print('Success! The MAC address has been changed!')
    else:
        print('The MAC address could not be changed : (')


mac_match(mac_address_search_result, options.new_mac)
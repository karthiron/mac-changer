#Mac_Changer_Tools
#Written By Karthikeyan
import subprocess
import optparse
import re

def get_options():
    menu = optparse.OptionParser()
    menu.add_option("-i", "--interface", dest="interface", help="Used to select interface")
    menu.add_option("-m", "--mac", dest="new_mac", help="Used to Select Mac")
    (options, arguments) = menu.parse_args()
    if not options.interface:
        menu.error("Interface is not specified!! use --help to get more information")
    elif not options.new_mac:
        menu.error("MAC Address is not specified!! use --help to get more information")
    else:
        return options

def changing_mac(interface, new_mac):
    print("Changing MAC Address " + interface + " To " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if filter_result:
        return filter_result.group(0)
    else:
        print("MAC Address Not Found")

options = get_options()

mac_address = get_mac_address(options.interface)

print("Current MAC = " + str(mac_address))

changing_mac(options.interface, options.new_mac)

mac_address = get_mac_address(options.interface)

if mac_address == options.new_mac:
    print("MAC Address Changed To :" + mac_address)
else:
    print("Mac Address Is Not Changed")

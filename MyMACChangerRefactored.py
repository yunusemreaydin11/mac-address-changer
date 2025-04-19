import subprocess
import optparse
import re


def get_user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest ="interface",help = "interface to change!" )
    parse_object.add_option("-m","--mac", dest = "mac", help ="New Mac Address" )
    return parse_object.parse_args()


def change_mac_address(user_interface,user_mac):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether", user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])

def mac_control(interface):
    ifconfig = subprocess.check_output(["ifconfig" ,interface])
    changed_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if changed_mac_address:
        return changed_mac_address.group(0)
    else:
        return None


print("Mac Changer Started!")

(user_input,arguments) = get_user_inputs()
change_mac_address(user_input.interface,user_input.mac)
final_mac = mac_control(user_input.interface)

if final_mac == user_input.mac:
    print("Success")
else:
    print("Error!")


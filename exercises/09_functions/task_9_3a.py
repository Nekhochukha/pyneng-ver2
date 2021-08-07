# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
filename = "config_sw2.txt"

def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as src:
        for line in src:
            if line.rstrip() and not "!" in line:
                if "thernet" in line:
                    num_intf = line.split()[1]
                elif "access vlan" in line:
                    access_dict[num_intf] = int(line.split()[-1])
                elif "mode access" in line:
                    access_dict[num_intf] = 1
                elif "allowed vlan" in line:
                    trunk_dict[num_intf] = [int(n) for n in line.split()[-1].split(',')]
    return access_dict, trunk_dict
print(get_int_vlan_map(filename))


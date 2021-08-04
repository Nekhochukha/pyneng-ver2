# -*- coding: utf-8 -*-
"""
Task 6.3

A configuration generator for access ports is made in the script.
Make a similar configuration generator for trunk ports.

In trunks, the situation is complicated by the fact that there can be many VLANs,
and you need to understand what to do with them (add, delete, overwrite).

Therefore, in accordance with each port there is a list and the first (zero index)
element of the list specifies how to interpret VLAN numbers that follow.


Dict value and corresponding command:
* ['add', '10', '20'] - switchport trunk allowed vlan add 10,20
* ['del', '17'] - switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - switchport trunk allowed vlan 11,30

Task for ports 0/1, 0/2, 0/4, 0/5, 0/7:
- generate a configuration based on the trunk_template template
- taking into account the keywords add, del, only

The code should not be tied to specific port numbers. I.e,
if there are other interface numbers in the trunk dictionary, the code should work.

For data in the trunk_template dictionary, output to
the standard output should be like this:
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,21
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}
#print(trunk.items())
for intf, vlan_cmd in trunk.items():
    print(f"interface FastEthernet {intf}")
    if vlan_cmd[0] == 'add':
        vlan_cmd_end = 'add ' + ','.join(vlan_cmd[1:])
    if vlan_cmd[0] == 'del':
        vlan_cmd_end = 'remove ' + ','.join(vlan_cmd[1:])
    if vlan_cmd[0] == 'only':
        vlan_cmd_end = ','.join(vlan_cmd[1:])

    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(f" {command} {vlan_cmd_end}")
        else:
            print(f" {command}")
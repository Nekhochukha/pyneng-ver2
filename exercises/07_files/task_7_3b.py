# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
line_list_full = []
vlans = []
with open('CAM_table.txt', 'r') as src:
    for line in src:
        line_list = line.split()
        if line_list and line_list[0].isdigit():
            vlan = line_list[0]
            mac = line_list[1]
            interface = line_list[3]
            line_list_full.append([int(vlan), mac, interface])
            vlans.append(int(vlan))

vlans = list(set(vlans))
#print(vlans)
vlan_input = input(f"Enter VLAN number {vlans}:")

for i in sorted(line_list_full):
    if i[0] == int(vlan_input):
        vlan = i[0]
        mac = i[1]
        interface = i[2]
        print(f"{vlan:<10}{mac:20}{interface}")
    else:
        continue

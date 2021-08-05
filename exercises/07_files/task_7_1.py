# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

['O', '10.0.24.0/24', '[110/41]', 'via', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']
['O', '10.0.28.0/24', '[110/31]', 'via', '10.0.13.3,', '3d20h,', 'FastEthernet0/0']
['O', '10.0.37.0/24', '[110/11]', 'via', '10.0.13.3,', '3d20h,', 'FastEthernet0/0']
['O', '10.0.41.0/24', '[110/51]', 'via', '10.0.13.3,', '3d20h,', 'FastEthernet0/0']
['O', '10.0.78.0/24', '[110/21]', 'via', '10.0.13.3,', '3d20h,', 'FastEthernet0/0']
['O', '10.0.79.0/24', '[110/20]', 'via', '10.0.19.9,', '4d02h,', 'FastEthernet0/2']

"""
with open('ospf.txt') as f:
    for line in f:
        line_list = line.split()
        #print(line.split())
        print(f"Prefix{'':20}{line_list[1]}")
        print(f"AD/Metric{'':17}{line_list[2].strip('[]')}")
        print(f"Next-Hop{'':18}{line_list[4].rstrip(',')}")
        print(f"Last update{'':15}{line_list[5].rstrip(',')}")
        print(f"Outbound Interface{'':8}{line_list[6]}")

'''
Вместо strip and rstrip можно было сразу всю строку подготовить
line_list = line.replace(",", " ").replace("[", "").replace("]", "")
'''

# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip = input('Введите IP адрес: ')
#ip = '10.1.16.50'

oct1, oct2, oct3, oct4 = ip.split('.')

if 1 <= int(oct1) <= 223:
    print("unicast")
elif 224 <= int(oct1) <= 239:
    print("multicast")
elif ip == '255.255.255.255':
    print("local broadcast")
elif ip == '0.0.0.0':
    print("unassigned")
else:
    print("unused")


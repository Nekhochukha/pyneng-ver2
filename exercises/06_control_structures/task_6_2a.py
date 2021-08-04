# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input('Введите IP адрес: ')
#ip = '10.1.16.50'
ip_list = ip.split('.')
correct_ip = False

if len(ip_list) == 4:
    for oct in ip_list:
        if oct.isdigit() and 0 <= int(oct) <= 255:  #in range(256) вместо 0 <= int(oct) <= 255
            correct_ip = True
        else:
            correct_ip = False
            break

if correct_ip:
    oct1 = ip_list[0]
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
else:
    print('Invalid IP address')

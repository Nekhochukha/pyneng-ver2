# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input('Введите IP адрес: ')
correct_ip = False

while not correct_ip:

    ip_list = ip.split('.')

    if len(ip_list) == 4:
        for oct in ip_list:
            if oct.isdigit() and int(oct) in range(256):
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
        ip = input('Введите IP адрес еще раз: ')
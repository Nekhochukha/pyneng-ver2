ip = input('Введите IP адрес: ')
#ip = '10.1.16.50'
ip_list = ip.split('.')
correct_ip = False

if len(ip_list) == 4:
    for oct in ip_list:
        if oct.isdigit() and 0 <= int(oct) <= 255:
            correct_ip = True
        else:
            correct_ip = False

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
    print('Неправильный IP-адрес')
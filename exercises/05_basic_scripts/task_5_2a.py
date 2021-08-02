# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

net_addr_mask = input('Введите адрес сети в формате "10.1.1.0/24": ')
#net_addr_mask = '10.1.1.195/28'
mask_net = net_addr_mask.split('/')[-1]
addr_host = net_addr_mask.split('/')[0]
#Разбиваем адрес на октеты
oct1, oct2, oct3, oct4 = addr_host.split('.')
#Преобразуем адрес в 32 битное значение
addr_host_b = f'{int(oct1):08b}{int(oct2):08b}{int(oct3):08b}{int(oct4):08b}'
#Преобразуем маску в 32 битное значение
mask_b = int(mask_net) * '1' + (32-int(mask_net)) * '0'
#Получаем адрес сети согласно маске (заменяем нулями биты в введенном адресе сверх маски)
addr_net_b_from_mask = addr_host_b[0:int(mask_net)] + (32-int(mask_net)) * '0'
#Получаем десятичные значения октетов адреса сети
ipnet_oct1 = int(addr_net_b_from_mask[0:8], 2)
ipnet_oct2 = int(addr_net_b_from_mask[8:16], 2)
ipnet_oct3 = int(addr_net_b_from_mask[16:24], 2)
ipnet_oct4 = int(addr_net_b_from_mask[24:32], 2)

tmpl_network ='''
Network:
{0:<10d}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
#Получаем десятичные значения октетов маски сети
mask_oct1 = int(mask_b[0:8], 2)
mask_oct2 = int(mask_b[8:16], 2)
mask_oct3 = int(mask_b[16:24], 2)
mask_oct4 = int(mask_b[24:32], 2)

tmpl_mask ='''
Mask:
/{0}
{1:<10d}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
#
#print(type(mask_net), type(addr_net))
#print(mask_net, addr_net.split('.'))
print(tmpl_network.format(ipnet_oct1, ipnet_oct2, ipnet_oct3, ipnet_oct4))
print(tmpl_mask.format(mask_net, mask_oct1, mask_oct2, mask_oct3, mask_oct4))
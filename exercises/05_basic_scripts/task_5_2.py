# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

net_addr_mask = input('Введите адрес сети в формате "10.1.1.0/24": ')
#net_addr_mask = '10.1.1.0/20'
mask_net = net_addr_mask.split('/')[-1]
addr_net = net_addr_mask.split('/')[0]
oct1, oct2, oct3, oct4 = addr_net.split('.')
oct1 = int(oct1)
oct2 = int(oct2)
oct3 = int(oct3)
oct4 = int(oct4)
tmpl_network ='''
Network:
{0:<10d}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
mask_b = int(mask_net) * '1' + (32-int(mask_net)) * '0'
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
print(tmpl_network.format(oct1, oct2, oct3, oct4))
print(tmpl_mask.format(mask_net, mask_oct1, mask_oct2, mask_oct3, mask_oct4))
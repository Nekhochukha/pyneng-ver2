'''
Ethernet0/1 is up, line protocol is up
Internet address is 192.168.200.1/24
Broadcast address is 255.255.255.255
Address determined by non-volatile memory
MTU is 1500 bytes
Helper address is not set
'''
result = {}
with open('/home/python/pyneng-ver2/exercises/07_files/sh_ip_interface.txt') as f:
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
            result[interface] = {}
        elif 'Internet address' in line:
            ip_address = line.split()[-1]
            result[interface]['ip'] = ip_address
        elif 'MTU is' in line:
            mtu = line.split()[-2]
            result[interface]['mtu'] = mtu

print(result)
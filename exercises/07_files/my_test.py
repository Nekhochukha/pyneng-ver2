
result = {}
with open('/home/python/pyneng-ver2/exercises/07_files/sh_ip_int_br.txt') as f:
    for line in f:
        line = line.split()


        if line and line[1][0].isdigit():
            interface, address, *other = line
            print(interface, address, other)
            result[interface] = address

print(result)

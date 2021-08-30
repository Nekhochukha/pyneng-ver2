dict01 = {
   ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
   ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
   ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
   ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
   ("R3", "Eth0/1"): ("R4", "Eth0/0"),
   ("R3", "Eth0/2"): ("R5", "Eth0/0"),
   ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
   ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
   ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
   ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
   }

keys_dict = dict01.keys()
dict02 = dict01.copy()
dict03 = {}
for key, value in dict01.items():
    if value in keys_dict:
        dict03[value] = key
        del dict02[value]
        del dict02[key]
        keys_dict = dict02.keys()

dict02.update(dict03)
print(dict02)
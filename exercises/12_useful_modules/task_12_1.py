# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(ipaddr_list):

    yes_ip = []
    no_ip = []
    for ip in ipaddr_list:
        print('ping:', ip)
        pr_run = subprocess.run(['ping', ip, '-c', '3'], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
        if pr_run.returncode == 0:
            yes_ip.append(ip)
        else:
            no_ip.append(ip)
    return yes_ip, no_ip

if __name__ == "__main__":
    ipaddr_list = ['127.0.0.1', '8.8.8.8', '192.168.0.1', '10.1.1.1']
    print(ping_ip_addresses(ipaddr_list))
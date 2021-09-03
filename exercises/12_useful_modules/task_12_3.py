# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
import subprocess
from tabulate import tabulate

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
def print_ip_table(reach, unreach):
    #columns = ['Reachable', 'Unreachable']
    #all_list = []
    #all_list.append(reach)
    #all_list.append(unreach)
    #ip_dict = dict(zip(columns, all_list))
    table = {'Reachable' : reach, 'Unreachable' : unreach}
    print(tabulate(table, headers='keys'))


if __name__ == "__main__":
    ipaddr_list = ['127.0.0.1', '8.8.8.8', '192.168.0.1', '10.1.1.1']
    ipaddr_tuple = ping_ip_addresses(ipaddr_list)
    reach_l, unreach_l = ipaddr_tuple
    print_ip_table(reach_l, unreach_l)
# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

from sys import argv

filename = argv[1]

ignore = ["duplex", "alias", "configuration"]

#filename = "config_sw1.txt"

with open(filename, 'r') as f:
    for line in f:
        if '!' in line:
            pass
        elif ignore[0] in line or ignore[1] in line or ignore[2] in line:
            pass
        elif not line.rstrip():
            pass
        else:
            print(line.rstrip())

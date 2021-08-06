# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""


from sys import argv

filename_src = argv[1]
filename_dst = argv[2]


ignore = ["duplex", "alias", "configuration"]


with open(filename_src, 'r') as src,  open(filename_dst, 'w') as dst:
    for line in src:
        if '!' in line:
            pass
        elif ignore[0] in line or ignore[1] in line or ignore[2] in line:
            pass
        elif not line.rstrip():
            pass
        else:
           # print(line.rstrip())
           dst.write(line)

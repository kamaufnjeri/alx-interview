#!/usr/bin/python3
"""This script reads lines from stdin in this format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
and after every 10 lines or keyboard interruption
it prints File size: <total size>
<status code>: <number> for every status code"""

from sys import stdin


try:
    my_dict = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        parts = line.split(" ")
        try:
            total_size += int(parts[-1])
            status = int(parts[-2])
            if status not in my_dict:
                my_dict[status] = 1
            else:
                my_dict[status] += 1
        except (ValueError, IndexError):
            continue
        my_dict = dict(sorted(my_dict.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in my_dict.items():
                print("{}: {}".format(key, val))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))

#!/usr/bin/python3
"""This script reads lines from stdin in the specified format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
and after every 10 lines or keyboard interruption,
it prints File size: <total size>
<status code>: <number> for every status code"""

from sys import stdin

try:
    status_code_count = {}
    total_file_size = 0

    for line_num, line in enumerate(stdin, start=1):
        line_parts = line.split(" ")

        try:
            file_size = int(line_parts[-1])
            status = int(line_parts[-2])

            total_file_size += file_size

            if status not in status_code_count:
                status_code_count[status] = 1
            else:
                status_code_count[status] += 1

        except (ValueError, IndexError):
            continue

        status_code_count = dict(sorted(status_code_count.items()))

        if line_num % 10 == 0:
            print("File size: {}".format(total_file_size))
            for key, count in status_code_count.items():
                print("{}: {}".format(key, count))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_file_size))
    for key, count in status_code_count.items():
        print("{}: {}".format(key, count))

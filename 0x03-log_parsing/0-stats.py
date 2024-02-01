#!/usr/bin/python3
"""Reads lines from stdin in the format: <IP> - [<date>]
 "GET /projects/260 HTTP/1.1" <status> <size>
Prints metrics after every 10 lines or keyboard interruption:
File size: <total size>
<status>: <count> for each status code."""

from sys import stdin

try:
    status_counts = {}
    total_size = 0

    for line_num, line in enumerate(stdin, start=1):
        parts = line.split(" ")

        try:
            total_size += int(parts[-1])
            status_code = int(parts[-2])

            if status_code not in status_counts:
                status_counts[status_code] = 1
            else:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            continue

        status_counts = dict(sorted(status_counts.items()))

        if line_num % 10 == 0:
            print("File size: {}".format(total_size))
            for key, count in status_counts.items():
                print("{}: {}".format(key, count))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, count in status_counts.items():
        print("{}: {}".format(key, count))

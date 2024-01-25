#!/usr/bin/python3
"""Script for parsing HTTP request logs and computing metrics
"""

from sys import stdin

try:
    status_counts = {}
    total_file_size = 0

    for line_num, log_line in enumerate(stdin, start=1):
        log_parts = log_line.split(" ")

        try:
            file_size = int(log_parts[-1])
            status_code = int(log_parts[-2])

            total_file_size += file_size

            if status_code not in status_counts:
                status_counts[status_code] = 1
            else:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            continue

        status_counts = dict(sorted(status_counts.items()))

        if line_num % 10 == 0:
            print("Total file size: {}".format(total_file_size))
            for code, count in status_counts.items():
                print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("Total file size: {}".format(total_file_size))
    for code, count in status_counts.items():
        print("{}: {}".format(code, count))

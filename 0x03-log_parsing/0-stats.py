#!/usr/bin/python3
"""HTTP Log Parser

This script reads lines from stdin in the specified format and computes metrics.

Format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines or keyboard interruption, it prints:
- Total File Size: <total size>
- Status Code Counts: <status code>: <number> for every status code
"""

from sys import stdin

try:
    status_counts = {}
    accumulated_size = 0

    for line_number, log_line in enumerate(stdin, start=1):
        log_parts = log_line.split(" ")

        try:
            file_size = int(log_parts[-1])
            status_code = int(log_parts[-2])

            accumulated_size += file_size

            if status_code not in status_counts:
                status_counts[status_code] = 1
            else:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            continue

        status_counts = dict(sorted(status_counts.items()))

        if line_number % 10 == 0:
            print("Total File Size: {}".format(accumulated_size))
            for code, count in status_counts.items():
                print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("Total File Size: {}".format(accumulated_size))
    for code, count in status_counts.items():
        print("{}: {}".format(code, count))

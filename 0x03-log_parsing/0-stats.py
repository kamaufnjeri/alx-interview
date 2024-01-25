#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys
import signal

def print_stats(total_size, status_codes):
    """
    Print statistics based on total file size and lines by status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """
    Signal handler to print stats on interrupt (CTRL + C).
    """
    print_stats(total_size, status_codes)
    sys.exit(0)

def parse_line(line, total_size, status_codes):
    """
    Parse a log line and update total file size and status code counts.
    """
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        return total_size, status_codes

    except (ValueError, IndexError):
        return total_size, status_codes

if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(line.strip(), total_size, status_codes)

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()  # Wait for the interrupt signal

    print_stats(total_size, status_codes)

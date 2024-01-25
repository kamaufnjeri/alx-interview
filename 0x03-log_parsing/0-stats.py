#!/usr/bin/python3
'''Script for parsing HTTP request logs and computing metrics.
'''

import re


def extract_log_info(log_line):
    '''Extracts sections of a line from an HTTP request log.'''
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_format = '{}\\-{}{}{}{}\\s*'.format(*log_pattern)
    match = re.fullmatch(log_format, log_line)
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_metrics(total_size, status_codes):
    '''Prints the accumulated metrics of the HTTP request log.'''
    print('Total file size: {:d}'.format(total_size), flush=True)
    for code in sorted(status_codes.keys()):
        count = status_codes.get(code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(code, count), flush=True)


def update_metrics(line, total_size, status_codes):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_log_info(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes.keys():
        status_codes[status_code] += 1
    return total_size + line_info['file_size']


def run():
    '''Starts the log parser.'''
    line_count = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            log_line = input()
            total_file_size = update_metrics(
                log_line,
                total_file_size,
                status_codes_stats,
            )
            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_metrics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

#!/usr/bin/python3

import sys
from collections import defaultdict

"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""



def print_stats(lines):
    """
    Print file size and status code statistics for the given lines.
    
    Args:
        lines (list): A list of lines to process.
    """
    total_size = 0
    status_count = defaultdict(int)

    for line in lines:
        ip_address, _, _, date, _, method, status_code, file_size = line.strip().split(" ")
        total_size += int(file_size)
        status_count[status_code] += 1

    print(f"Total file size: File size: {total_size}")
    for status in sorted(status_count):
        print(f"{status}: {status_count[status]}")

try:
    lines = []
    for line in sys.stdin:
        lines.append(line)
        if len(lines) >= 10:
            print_stats(lines)
            lines = []

    if lines:
        print_stats(lines)
except KeyboardInterrupt:
    print_stats(lines)
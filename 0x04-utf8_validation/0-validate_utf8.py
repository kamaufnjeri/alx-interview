#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: A list of integers representing 1 byte of data each.

    Returns:
    - True if data is a valid UTF-8 encoding, else False
    """

    def is_start_of_char(num):
        return (
            num & 0b10000000
        ) == 0b10000000 and (num & 0b01000000) == 0b00000000

    following_bytes = 0

    for byte in data:
        if following_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                following_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                following_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                following_bytes = 3
            else:
                return False
        else:
            if not is_start_of_char(byte):
                return False
            following_bytes -= 1

    return following_bytes == 0

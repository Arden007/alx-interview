#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: A list of int's where each integer represents 1 byte of data.
    :return: True if data is a valid UTF-8 encoding, else return False.
    """

    # Init a variable to keep track of the number of expected following bytes
    next_byte = 0

    for byte in data:
        if next_byte == 0:
            print(byte , "= in binary: " , bin(byte >> 5))
            # Check the most significant bits of the byte,
            # to determine the number of following bytes.
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                # Two-byte or three-byte character
                next_byte = 1
            elif byte >> 4 == 0b1110:
                # Four-byte character
                next_byte = 2
            elif byte >> 3 == 0b11110:
                # Five-byte character
                next_byte = 3
            elif byte >> 7 != 0b0:
                # If the most significant bit is not 0,
                # it's not a valid start of a character.
                return False
        else:
            # Check if the byte is a valid continuation byte (starts with 10)
            if byte >> 6 == 0b10:
                next_byte -= 1
            else:
                # If a continuation byte doesn't start with 10, it's not valid.
                return False

    # Check if all expected following bytes were found
    return next_byte == 0

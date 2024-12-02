# This script loops over all numbers and if there is an adjacent symbol it adds it to the sum

import re
import string

from collections import defaultdict
from functools import reduce


def get_symbol_matrix(lines):
    non_symbols = string.digits + '.'
    symbol_matrix = []
    for line in lines:
        symbol_matrix.append([x not in non_symbols for x in line])

    return symbol_matrix


def get_numbers_and_ranges(line):
    ret = []

    for m in re.finditer(r"\d+", line):
        ret.append((int(m.group(0)), m.span()))

    return ret


def get_valid_numbers(numbers_and_ranges, symbol_lines):
    valid_numbers = []

    for number, ranges in numbers_and_ranges:
        symbol_range = (max(0, ranges[0]-1), ranges[1]+1) # ranges[1]+1 could be out of bounds if the number is at the end of the line, but python handles this so I don't bother.
        for symbol_line in symbol_lines:
            if any(symbol_line[symbol_range[0]:symbol_range[1]]):
                valid_numbers.append(number)
                continue

    return valid_numbers


def main():
    sum = 0
    with open("input") as f:
        lines = [x.strip() for x in f.readlines()]

        symbol_matrix = get_symbol_matrix(lines)
        dummy_symbol_line = [False] * len(lines[0])
        for line_no, line in enumerate(lines):
            # Get the previous, current and next lines from the symbol matrix, special cases for first and last
            if line_no == 0:
                symbol_lines = [dummy_symbol_line] + symbol_matrix[line_no:line_no+2]
            elif line_no == len(lines):
                symbol_lines = symbol_matrix[line_no-1:line_no+1] + [dummy_symbol_line]
            else:
                symbol_lines = symbol_matrix[line_no-1:line_no+2]

            numbers_and_ranges = get_numbers_and_ranges(line)

            valid_numbers = get_valid_numbers(numbers_and_ranges, symbol_lines)

            for number in valid_numbers:
                sum += number

    print(sum)


if __name__ == '__main__':
    main()
    

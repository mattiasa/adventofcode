# This script loops over all asterisks and checks if there are exactly 2 adjacent numbers. If there are it multiplies them

import re
import string

from collections import defaultdict
from functools import reduce


def get_star_matrix(lines):
    symbols = "*"
    symbol_matrix = []
    for line in lines:
        symbol_matrix.append([x in symbols for x in line])

    return symbol_matrix


def get_numbers_and_ranges(line):
    ret = []

    for m in re.finditer(r"\d+", line):
        ret.append((int(m.group(0)), m.span()))

    return ret


def get_line_sum(symbol_line, number_lines):
    sum = 0

    for i, is_asterisk in enumerate(symbol_line):
        if is_asterisk:
            adjecent_numbers = []
            for number_line in number_lines:
                for number in number_line:
                    if i >= number[1][0]-1 and i <= number[1][1]:
                        adjecent_numbers.append(number[0])
            assert len(adjecent_numbers) <= 2
            
            if len(adjecent_numbers) == 2:
                sum += adjecent_numbers[0] * adjecent_numbers[1]

    return sum


def main():
    sum = 0
    with open("input") as f:
        lines = [x.strip() for x in f.readlines()]
        line_matrix = [get_numbers_and_ranges(x) for x in lines]
        symbol_matrix = get_star_matrix(lines)
        dummy_number_line = []

        for line_no, symbol_line in enumerate(symbol_matrix):
            # Get the previous, current and next lines from the symbol matrix, special cases for first and last

            if line_no == 0:
                number_lines = [dummy_number_line] + line_matrix[line_no:line_no+2]
            elif line_no == len(lines):
                number_lines = line_matrix[line_no-1:line_no+1] + [dummy_number_line]
            else:
                number_lines = line_matrix[line_no-1:line_no+2]

            sum += get_line_sum(symbol_line, number_lines)


    print(sum)


if __name__ == '__main__':
    main()
    

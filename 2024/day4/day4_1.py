import sys
import re


def rev(s):
    return s[::-1]


def make_reverse(horizontal):
    return [rev(x) for x in horizontal]


def make_vertical(horizontal):
    return [''.join(y) for y in zip(*[list(x) for x in horizontal])]


def make_diagonal(horizontal):
    diagonal_lines1 = []
    diagonal_lines2 = []

    for i, line in enumerate(horizontal):

        n = len(line)
        l1 = 'Z' * (n - i) + line[:i]
        l2 = line[i:] + 'Z' * i

        diagonal_lines1.append(l1)
        diagonal_lines2.append(l2)

    return make_vertical(diagonal_lines1) + make_vertical(diagonal_lines2)


def main():
    with open(sys.argv[1])  as f:
        horizontal = [x.strip() for x in f.readlines()]

    horizontal_reversed = make_reverse(horizontal)

    vertical = make_vertical(horizontal)
    vertical_reversed = make_reverse(vertical)

    diagonal1 = make_diagonal(horizontal)
    diagonal2 = make_diagonal(horizontal_reversed)

    diagonal1_reversed = make_reverse(diagonal1)
    diagonal2_reversed = make_reverse(diagonal2)

    all_lines = horizontal + horizontal_reversed + vertical + vertical_reversed + diagonal1 + diagonal2 + diagonal1_reversed + diagonal2_reversed

    count = 0

    for line in all_lines:
        count += len(re.findall('XMAS', line))

    print(count)

if __name__ == '__main__':
    main()
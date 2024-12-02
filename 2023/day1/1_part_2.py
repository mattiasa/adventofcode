import sys
import re


DIGIT_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


REVERSE_DIGIT_MAPPING = {x[::-1]: y for (x, y) in DIGIT_MAPPING.items()}


def get_digits(line):
    """
    Get the first and last digit of a line.

    Make sure to handle the oneight case by reversing the line and the match pattern
    """
    
    print(line)
    digit_match_pattern = f"(?:[0-9]|{'|'.join([x for x in DIGIT_MAPPING])})"
    reverse_digit_match_pattern = f"(?:[0-9]|{'|'.join([x[::-1] for x in DIGIT_MAPPING])})" # [::-1] reverses
    matches = re.findall(digit_match_pattern, line)
    reverse_matches = re.findall(reverse_digit_match_pattern, line[::-1])
    print(matches)
    print(reverse_matches)

    first = matches[0]
    last = reverse_matches[0]

    first = DIGIT_MAPPING.get(first, first)
    last = REVERSE_DIGIT_MAPPING.get(last, last)

    number = int(f"{first}{last}")

    return number


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            line = line.strip()
            #print(line)
            num = get_digits(line)
            print(f"{sum} += {num}")
            sum += num

            print(sum)
            print()


if __name__ == '__main__':
    main()

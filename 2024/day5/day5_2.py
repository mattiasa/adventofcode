import sys
from functools import cmp_to_key

page_order = set()

def compare(a, b):
    if f'{a}|{b}' in page_order:
        return -1
    if f'{a}|{b}' in page_order:
        return 1
    return 0


def main():

    total = 0

    with open(sys.argv[1]) as f:
        for line in f:
            if line == "\n":
                break
            page_order.add(line.strip())

        for line in f:
            line = line.strip()
            valid = True
            numbers = line.split(",")
            for i, n in enumerate(numbers):
                for m in numbers[i+1:]:
                    if f"{m}|{n}" in page_order:
                        valid = False
                        break
            if not valid:
                new_numbers = sorted(numbers, key=cmp_to_key(compare))

                # print(f'{numbers} -> {new_numbers}')

                total += int(new_numbers[len(new_numbers)//2])

    print(total)

if __name__ == '__main__':
    main()
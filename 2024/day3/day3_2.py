import sys
import re

MUL_PATTERN = re.compile(r'^(.*?)mul\((\d+),(\d+)\)(.*)')

def main():
    total = 0

    enabled = True

    with open(sys.argv[1]) as f:
        for data in f.readlines():
            # print(f"data: {data}")
            while m := re.match(MUL_PATTERN, data):
                discard = m.group(1)

                a = int(m.group(2))
                b = int(m.group(3))

                if 'do()' in discard:
                    enabled = True
                if "don't()" in discard:
                    enabled = False

                if enabled:
                    total += a * b

                data = m.group(4)

                # print(f"a: {a}")
                # print(f"b: {b}")
                # print(f"discard: {discard}")
                # print(f"data: {data}")
                # print()

    print(total)


if __name__ == '__main__':
    main()

import sys


def is_line_safe(line):
    start = line[1] - line[0]

    for i in range(1, len(line)):
        diff = line[i] - line[i-1]

        if (start > 0 and diff < 0) or (start < 0 and diff > 0) or diff == 0 or abs(diff) > 3:
            return False

    return True


def main():
    fn = sys.argv[1]

    total = 0

    with open(fn) as f:
        for line in f:
            l = [int(x) for x in line.split()]
            if is_line_safe(l):
                total += 1
                continue

            for i in range(0, len(l)):
                if is_line_safe(l[:i] + l[i+1:]):
                    total += 1
                    break


    print(total)


if __name__ == '__main__':
    main()
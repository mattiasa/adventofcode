import math
import re
import sys


def main():
    if len(sys.argv) == 1:
        fn = "input"
    else:
        fn = sys.argv[1]

    with open(fn) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()

            m = re.match(r"(\w+):\s+(.*)", line)

            if m.group(1) == 'Time':
                times = [int(x) for x in re.split("\s+", m.group(2))]
            if m.group(1) == 'Distance':
                distances = [int(x) for x in re.split("\s+", m.group(2))]

    print(times)
    print(distances)

    pairs = zip(times, distances)

    sum = 1

    for t, d in pairs:
        r1 = math.ceil(t / 2 + math.sqrt((t/2)**2 - d)) - 1
        r2 = math.floor(t / 2 - math.sqrt((t / 2) ** 2 - d)) + 1
        print(r1, r2)
        sum *= (r1-r2+1) # it's [r2, r1] inclusive

    print(sum)

if __name__ == '__main__':
    main()


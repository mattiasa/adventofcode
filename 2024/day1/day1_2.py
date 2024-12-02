import sys
from collections import Counter


def main():
    fn = sys.argv[1]
    list1 = []
    list2 = []
    with open(fn) as f:
        for l in f:
            a, b = l.split()
            list1.append(int(a))
            list2.append(int(b))

    c = Counter(list2)


    total = 0

    for x in list1:
        total += x * c[x]

    print(total)


if __name__ == '__main__':
    main()
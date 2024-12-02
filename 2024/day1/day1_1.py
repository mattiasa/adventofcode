import sys

def main():
    fn = sys.argv[1]
    list1 = []
    list2 = []
    with open(fn) as f:
        for l in f:
            a, b = l.split()
            list1.append(int(a))
            list2.append(int(b))

    total = 0
    for x, y in zip(sorted(list1), sorted(list2)):
        total += abs(x - y)

    print(total)


if __name__ == '__main__':
    main()
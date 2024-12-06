import sys

page_order = set()

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
            if valid:
                total += int(numbers[len(numbers)//2])

    print(total)

if __name__ == '__main__':
    main()
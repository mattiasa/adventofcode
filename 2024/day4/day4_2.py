import sys

def main():

    total = 0
    with open(sys.argv[1])  as f:
        m = [x.strip() for x in f.readlines()]

        for x in range(0, len(m[0])-2):
            for y in range(0, len(m)-2):
                if ((m[y][x] == 'M' and m[y+1][x+1] == 'A' and m[y+2][x+2] == 'S') or
                    (m[y][x] == 'S' and m[y+1][x+1] == 'A' and m[y+2][x+2] == 'M')):
                    print(f"MAS at {x}, {y}")
                    if ((m[y][x+2] == 'M' and m[y + 1][x + 1] == 'A' and m[y + 2][x] == 'S') or
                        (m[y][x+2] == 'S' and m[y + 1][x + 1] == 'A' and m[y + 2][x] == 'M')):
                        total += 1
    print(total)

if __name__ == '__main__':
    main()
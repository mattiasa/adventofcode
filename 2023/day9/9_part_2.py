import sys
import os

terminal_width = os.get_terminal_size()[0]

def print_matrix(matrix):
    for row in matrix:
        print(f"{str(row):^{terminal_width}s}")
    print()


def main():
    sum = 0
    if len(sys.argv) == 1:
        fn = "input"
    else:
        fn = sys.argv[1]

    inputs = []

    with open(fn) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()

            inputs.append([int(x) for x in line.split(" ")])

    for inp in inputs:
        print()
        print(f"Processing inputs {inp}")
        print()
        matrix = [list(inp)]
        current_row = matrix[0]

        while any(current_row):
            next_row = []
            for i, _ in enumerate(current_row[1:], start=1):
                v = current_row[i] - current_row[i-1]
                next_row.append(v)

            matrix.append(next_row)
            current_row = next_row

        print_matrix(matrix)

        assert len(matrix[-1]) > 0

        for i in range(len(matrix)-2, -1, -1):
            diff = matrix[i+1][0]
            prev_value = matrix[i][0]
            next_value = prev_value - diff
            matrix[i].insert(0, next_value)

        sum += matrix[0][0]

        print_matrix(matrix)

    print(f"Total sum {sum}")


if __name__ == '__main__':
    main()


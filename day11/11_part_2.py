import sys
import os

terminal_width = os.get_terminal_size()[0]

EMPTY_SCALE_FACTOR = 1_000_000


def print_matrix(matrix):
    for row in matrix:
        print(f"{str(row):^{terminal_width}s}")
    print()


def expand_matrix(matrix):

    expanded_rows = []
    expanded_columns = []

    row_count = len(matrix)
    column_count = len(matrix[0])  # assume all rows have the same length

    for y in range(row_count):
        if '#' not in matrix[y]:
            matrix[y] = ['E'] * column_count
            expanded_rows.append(y)

    for x in range(column_count):
        if '#' not in [c[x] for c in matrix]:
            for y in range(row_count):
                matrix[y][x] = 'E'
            expanded_columns.append(y)

    print_matrix(matrix)

    return matrix


def find_galaxy_coords(matrix):
    galaxy_coords = []

    x = 0
    for row_no, row in enumerate(matrix):
        # I'm cheating here and assuming the first column isn't empty, which I know it isn't for my input data. YMMV
        if matrix[row_no][0] == 'E':
            x += EMPTY_SCALE_FACTOR
            continue # continue since we know there are no galaxies in this row

        y = 0

        for column_no, colum in enumerate(matrix[row_no]):
            if matrix[row_no][column_no] == 'E':
                y += EMPTY_SCALE_FACTOR
                continue
            elif matrix[row_no][column_no] == '#':
                galaxy_coords.append((y, x))

            y += 1

        x += 1

    return galaxy_coords


def main():

    matrix = []

    if len(sys.argv) == 1:
        fn = "input"
    else:
        fn = sys.argv[1]

    with open(fn) as f:
        lines = f.readlines()

        for line_no, line in enumerate(lines):
            line = line.strip()

            matrix.append(list(line))

    matrix = expand_matrix(matrix)

    galaxy_coords = find_galaxy_coords(matrix)

    distances = 0

    # Build up a distance triangle between all pairs, and calculate the distances.
    # It doesn't matter if we calculate the distance x + y or diagonally.
    for x in range(len(galaxy_coords)):
        for y in range(x+1, len(galaxy_coords)):
            distances += abs(galaxy_coords[x][0]-galaxy_coords[y][0]) + abs(galaxy_coords[x][1]-galaxy_coords[y][1])

    print(distances)


if __name__ == '__main__':
    main()


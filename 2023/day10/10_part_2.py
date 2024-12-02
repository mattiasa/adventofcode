import sys
import os

terminal_width = os.get_terminal_size()[0]

START_CHAR = 'S'

CHAR_STEP_MAP = {
    '|': ((0, 1), (0, -1)),
    '-': ((1, 0), (-1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, 1), (-1, 0)),
    'F': ((0, 1), (1, 0))
}


def print_matrix(matrix):

    for row in matrix:
        print(f"{str(row):^{terminal_width}s}")
    print()


def find_starting_direction(matrix, start_pos):
    # Test all potential alternatives for S and check if any lead to a char that leads back.
    # That's our target direction to start in (we don't actually care what character S is to figure out the length
    for candidate_char, dirs in CHAR_STEP_MAP.items():
        for d in dirs:
            candidate_new_pos = calc_new_pos(start_pos, d)
            candidate_new_char = matrix[candidate_new_pos[1]][candidate_new_pos[0]]
            try:
                candidate_new_dirs = CHAR_STEP_MAP[candidate_new_char]
            except KeyError:
                continue
            for candidate_new_dir in candidate_new_dirs:
                reverse_pos = calc_new_pos(candidate_new_pos, (candidate_new_dir[0] * -1, candidate_new_dir[1] * -1))
                if reverse_pos == start_pos:
                    return candidate_new_pos


def calc_new_pos(current_pos, step_to_next):
    return tuple(map(sum, zip(current_pos, step_to_next)))


def walk(matrix, current_pos, previous_pos=None):
    next_pos = None

    current_char = matrix[current_pos[1]][current_pos[0]]

    print(f"{current_pos} = {current_char}")

    if current_char == 'S':
        # Either start or end
        if previous_pos:
            # at end
            return None

        # at start... need to figure out directions
        return find_starting_direction(matrix, current_pos)

    for next_step_offset in CHAR_STEP_MAP[current_char]:
        next_pos = calc_new_pos(current_pos, next_step_offset)
        if next_pos != previous_pos:
            return next_pos

    return next_pos


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

            matrix.append(line)

            try:
                column_no = line.index(START_CHAR)
                start = (column_no, line_no)
            except ValueError:
                pass

    print(start)
    print_matrix(matrix)
    print(matrix[start[1]][start[0]])

    current_pos = start
    previous_pos = None
    i = 0
    while True:
        next_pos = walk(matrix, current_pos, previous_pos)
        if not next_pos:
            break

        previous_pos = current_pos
        current_pos = next_pos
        i += 1


    print(i//2)


if __name__ == '__main__':
    main()


import re


MAX_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible(game_line):
    cube_sets = game_line.split("; ")
    for cube_set in cube_sets:
        cubes = cube_set.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")

            if int(count) > MAX_LIMITS[color]:
                return False

    return True


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Game (\d+): (.*)", line)
            game_no = int(m[1])
            game_line = m[2]

            if is_possible(game_line):
                sum += game_no

    print(sum)


if __name__ == '__main__':
    main()
    

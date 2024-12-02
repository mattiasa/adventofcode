import re

from collections import defaultdict
from functools import reduce
import operator


def get_power(game_line):
    per_color_max = defaultdict(lambda: 0)

    cube_sets = game_line.split("; ")
    for cube_set in cube_sets:
        cubes = cube_set.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            count = int(count)

            per_color_max[color] = max(per_color_max[color], count)

    return reduce(operator.mul, per_color_max.values())


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Game (\d+): (.*)", line)
            game_no = int(m[1])
            game_line = m[2]

            power = get_power(game_line)
            sum += power

    print(sum)


if __name__ == '__main__':
    main()
    

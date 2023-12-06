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


    # sum = 0
    with open("input") as f:
        lines = f.readlines()
        card_counts = [1] * len(lines)
        for line in lines:
            line = line.strip()
#            print(f"X{line}X")
#:\s+(.*)\s+\|\+s(.*)
            m = re.match(r"Card\s+(\d+):\s+(.*)\s+\|\s+(.*)", line)
#            print(m[1])
#            print(m[2])
#            print(m[3])

            card_no = int(m[1])
            card_index = card_no - 1
#            print(card_no)
            winning_numbers = set(re.split("\s+", m[2]))
#            print(winning_numbers)
            my_numbers = set(re.split("\s+", m[3]))
#            print(my_numbers)

            my_hits = winning_numbers & my_numbers

            #print(card_counts)
            card_count = card_counts[card_index]
            print(f"{card_no} {len(my_hits)} {card_count}")

            for i in range(card_index + 1, min(card_index + 1 + len(my_hits), len(lines))):
                print(f" {i} +{card_count}")
                card_counts[i] += card_count

            #card_score = 2 ** (len(my_hits) - 1)
            # sum += card_score

#            print(f"{card_no}: {len(winning_numbers)}")

#            print("Winners: {}".format((winning_numbers & my_numbers)))
#            print(len(winning_numbers & my_numbers))

#            power = get_power(game_line)


    print(sum(card_counts))


if __name__ == '__main__':
    main()
    

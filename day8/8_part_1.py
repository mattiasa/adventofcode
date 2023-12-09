import sys
import re


def main():
    path_map = {}

    sum = 0
    if len(sys.argv) == 1:
        fn = "input"
    else:
        fn = sys.argv[1]

    with open(fn) as f:
        lines = f.readlines()

        rl_seq = lines[0].strip()
        
        for line in lines[1:]:

            line = line.strip()

            # ignore empty lines
            if not line:
                print("skipping")
                continue

            if m := re.match(r"(\w+) = \((\w+), (\w+)\)", line):
                source = m.group(1)
                dest_l = m.group(2)
                dest_r = m.group(3)

                path_map[source] = (dest_l, dest_r)

    current_source = 'AAA'

    i = 0

    rl_seq_iter = iter(rl_seq)

    while current_source != 'ZZZ':
        i += 1
        try:
            current_dir = next(rl_seq_iter)
        except StopIteration:
            # Start over from the beginning
            rl_seq_iter = iter(rl_seq)
            current_dir = next(rl_seq_iter)

        if current_dir == 'L':
            next_source = path_map[current_source][0]
        elif current_dir == 'R':
            next_source = path_map[current_source][1]
        else:
            print(f"Wrong dir in sequence {current_dir}")

        print(f"{i} {current_source} -> {next_source}")
        current_source = next_source


    print(i)


if __name__ == '__main__':
    main()


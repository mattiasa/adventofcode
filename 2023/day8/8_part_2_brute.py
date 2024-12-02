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

    # current_source = 'AAA'

    current_sources = tuple([x for x in path_map if x.endswith('A')])
    print(current_sources)

    visited = set()
    i = 0
    rl_seq_iter = iter(rl_seq)

    while not all([x.endswith('Z') for x in current_sources]):
        i += 1
        try:
            current_dir = next(rl_seq_iter)
        except StopIteration:
            # Start over from the beginning
            rl_seq_iter = iter(rl_seq)
            current_dir = next(rl_seq_iter)

        if current_dir == 'L':
            next_sources = tuple(path_map[x][0] for x in current_sources)
        elif current_dir == 'R':
            next_sources = tuple(path_map[x][1] for x in current_sources)
        else:
            print(f"Wrong dir in sequence {current_dir}")

        # print(f"{i} {current_sources} -> {next_sources}")
        # print(current_sources)

        #if next_sources in visited:
        #    print(f"{next_sources} already visited")
        #    break

        # visited.add(next_sources)

        current_sources = next_sources

        if i % 100000 == 0:
            print(i)

        #if i > 1_000_000:
        #    break

    print(i)


if __name__ == '__main__':
    main()


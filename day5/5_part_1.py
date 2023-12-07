import re
from collections import namedtuple

Range = namedtuple('Range', ['source_start', 'destination_start', 'length'])

class Range:
    def __init__(self, source_start, destination_start, length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.length = length

    def is_in_range(self, number):
        # print(f"{self.source_start}")
        return self.source_start <= number < self.source_start + self.length

    def map_number(self, number):
        if self.is_in_range(number):
            return self.destination_start + (number - self.source_start)

class RangeMap:
    def __init__(self):
        self.ranges = []

    def add_range(self, range):
        self.ranges.append(Range(destination_start=range[0], source_start=range[1], length=range[2]))

    def map_number(self, source_number):
        for range in self.ranges:
            if range.is_in_range(source_number):
                #print(f"{source_number} is in range")
                return range.map_number(source_number)

        print(f"{source_number} is not in range")
        return source_number

def main():

    source_destination_map = {}
    ranges_map = {}

    with open("input") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if m := re.match(r"seeds: (.*)", line):
                seeds = [int(x) for x in m.group(1).split(" ")]

            if m := re.match(r"(\w+)-to-(\w+) map:", line):
                source = m.group(1)
                destination = m.group(2)
                source_destination_map[source] = destination
                range_map_key = (source, destination)
                ranges_map[range_map_key] = RangeMap()

            if m := re.match(r"([0-9].*)", line):
                range_match = [int(x) for x in m.group(1).split(" ")]
                # print(f"rm {range_match}")
                ranges_map[range_map_key].add_range(range_match)

    min_location = None
    for seed in seeds:

        source = 'seed'
        source_number = seed
        while source != 'location':

            destination = source_destination_map[source]

            destination_number = ranges_map[(source, destination)].map_number(source_number)

            print(f" {source} {source_number} {destination} {destination_number}")

            source = destination
            source_number = destination_number

        if min_location is not None:
            min_location = min(min_location, destination_number)
        else:
            min_location = destination_number

        print(min_location)


if __name__ == '__main__':
    main()

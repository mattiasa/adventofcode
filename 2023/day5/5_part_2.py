import json
import sys
import re
from collections import namedtuple
from itertools import chain

Range = namedtuple('Range', ['source_start', 'destination_start', 'length'])

class Range:
    def __init__(self, source_start, destination_start, length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.length = length

    def __repr__(self):
        return f"Range: {self.source_start}:{self.source_start + self.length} -> {self.destination_start}:{self.destination_start + self.length} "

    def is_in_range(self, number):
        # print(f"{self.source_start}")
        return self.source_start <= number < self.source_start + self.length

    def map_number(self, number):
        if self.is_in_range(number):
            return self.destination_start + (number - self.source_start)

class RangeMap:
    def __init__(self, source, destination):
        self.ranges = []
        self.source = source
        self.destination = destination

    def __repr__(self):
        r = '\n  '.join([repr(x) for x in self.ranges])
        return f"RangeMap: {self.source} -> {self.destination}\n  {r}"

    def add_range(self, range):
        self.ranges.append(Range(destination_start=range[0], source_start=range[1], length=range[2]))
        #yea, it's inefficient to do this on every insert
        self.ranges = sorted(self.ranges, key=lambda x: x.source_start)

    def map_number(self, source_number):
        for range in self.ranges:
            if range.is_in_range(source_number):
                #print(f"{source_number} is in range")
                return range.map_number(source_number)

        print(f"{source_number} is not in range")
        return source_number

    def split_range(self, source_range):
        import ipdb; ipdb.set_trace()
        for range in self.ranges:
            if source_range
            print(range)


def find_lowest_location(range_maps, source_destination_map, source_range, source='seed'):
    # base case
    if source == 'location':
        return source_range[0]

    destination = source_destination_map[source]

    # split ranges

    min_location = sys.maxsize

    for range in split_ranges(range_maps, source_range, source, destination):
        min_location = min(min_location, find_lowest_location(range_maps, source_destination_map, range, destination))

    return min_location

def main():
    if len(sys.argv) == 1:
        fn = "input"
    else:
        fn = sys.argv[1]
    source_destination_map = {}
    range_maps = {}

    with open(fn) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if m := re.match(r"seeds: (.*)", line):
                seed_numbers = [int(x) for x in m.group(1).split(" ")]
                number_of_seeds = sum(seed_numbers[0::2])
                #break
                seed_ranges = [range(x, x + y) for x, y in zip(seed_numbers[0::2], seed_numbers[1::2])]
#                seeds = list([range(x, x + y) for x, y in zip(seed_numbers[0::2], seed_numbers[1::2])])
                #print(seeds)

            if m := re.match(r"(\w+)-to-(\w+) map:", line):
                source = m.group(1)
                destination = m.group(2)
                source_destination_map[source] = destination
                range_map_key = (source, destination)
                range_maps[range_map_key] = RangeMap(source=source, destination=destination)

            if m := re.match(r"([0-9].*)", line):
                range_match = [int(x) for x in m.group(1).split(" ")]
                # print(f"rm {range_match}")
                range_maps[range_map_key].add_range(range_match)

    # Sort the ranges on the start value
#    for key, value in range_maps.items():
#        range_maps[key] = sorted(range_maps[key], key=lambda x: x[0])

    #print(range_maps)
    for key, value in range_maps.items():
        print(key)
        print(value)


    # A very large number
    min_location = sys.maxsize
    i = 0
    for seed_range in seed_ranges:
        #print(seed)
        import ipdb; ipdb.set_trace()
        min_location = min(find_lowest_location(range_maps, source_destination_map, seed_range))

        source = 'seed'
        source_number = seed
        while source != 'location':

            destination = source_destination_map[source]

            destination_number = range_maps[(source, destination)].map_number(source_number)

            #print(f" {source} {source_number} {destination} {destination_number}")

            source = destination
            source_number = destination_number

        if min_location is not None:
            min_location = min(min_location, destination_number)
        else:
            min_location = destination_number

        i += 1
        if i % 1000 == 0:
            print(f"{i} {i/number_of_seeds}")

        # print(min_location)


if __name__ == '__main__':
    main()

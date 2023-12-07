import sys
from collections import Counter

CARD_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def hand_key_func(key):

    hand, bid = key

    c = Counter(hand)
    c_values = c.values()

    if 5 in c_values:
        return 6
    if 4 in c_values:
        return 5
    if 3 in c_values and 2 in c_values:
        return 4
    if 3 in c_values:
        return 3
    if 2 in c_values and len(c_values) == 3: # two pairs
        return 2
    if 2 in c_values:
        return 1

    return 0


def card_key_func(key):
    hand, bid = key

    return [CARD_ORDER.index(x) for x in hand]


def main():
    sum = 0
    if len(sys.argv) == 1:
        fn = "input"
    else:
        fn = sys.argv[1]

    hand_bids = []

    with open(fn) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()

            hand, bid = line.split(" ")
            bid = int(bid)

            hand_bids.append((hand, bid))

    # Use the two sorting functions above. This relies on python's stable sorting property
    hand_bids_by_card = sorted(hand_bids, key=card_key_func)
    hand_bids_by_suite = sorted(hand_bids_by_card, key=hand_key_func)

    for rank, (hand, bid) in enumerate(hand_bids_by_suite, start=1):
        sum += rank * bid

    print(sum)


if __name__ == '__main__':
    main()


import sys
from collections import Counter

CARD_ORDER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def hand_key_func(key):
    """
    Sort function for ordering by hand type.

    Returns the following values:
    6 for 5-of-a-kind
    5 for 4-of-a-kind
    4 for full house
    3 for 3-of-a-kind
    2 for 2-pair
    1 for single pair
    0 for high card
    """
    hand, bid = key

    c = Counter(hand)
    c_values = list(c.values())

    j_count = c.get('J', 0)
    try:
        del c['J']
    except KeyError:
        pass

    c_without_j_added = list(c.values())

    c_with_j_added = [x + j_count for x in c.values()]
    if 5 in c_values or 5 in c_with_j_added:
        return 6
    if 4 in c_values or 4 in c_with_j_added:
        return 5
    if 3 in c_values and 2 in c_values:
        return 4
    if c_without_j_added == [2, 2] and j_count == 1: # special case of full house with a joker
        return 4
    if 3 in c_values or 3 in c_with_j_added:
        return 3
    if 2 in c_values and len(c_values) == 3: # two pairs. We can never have that with a J either as that would become a 3 of a kind
        return 2
    if 2 in c_values or 2 in c_with_j_added:
        return 1

    return 0


def card_key_func(key):
    """
    Sort function for card values

    Returns a 5-element list with the index of each card in CARD_ORDER.

    Since lists are compared element by element this works as a key function.
    """
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
    # https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
    hand_bids_by_card = sorted(hand_bids, key=card_key_func)
    hand_bids_by_suite = sorted(hand_bids_by_card, key=hand_key_func)

    for rank, (hand, bid) in enumerate(hand_bids_by_suite, start=1):
        sum += rank * bid

    print(sum)


if __name__ == '__main__':
    main()


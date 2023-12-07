POINTS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}
POINTS.update({f'{x}': x for x in reversed(range(2, 10))})

HAND_TYPES = {
    '5': 7,
    '4': 6,
    'FH': 5,
    '3': 4,
    '2': 3,
    '1': 2,
    'H': 1
}


def determine_hand_type(cards, calculate_joker=False):
    card_map = {}
    jokers = 0
    for _card in cards:
        if _card == 'J' and calculate_joker:
            jokers += 1
        else:
            card_map[_card] = card_map.get(_card, 0) + 1

    if calculate_joker:
        highest_occurrence_card = list(card_map.keys())[0] if len(card_map.keys()) else 'J'
        for card, occurrence in card_map.items():
            if occurrence > card_map[highest_occurrence_card]:
                highest_occurrence_card = card

        card_map[highest_occurrence_card] = card_map.get(highest_occurrence_card, 0) + jokers

    unique_cards = len(card_map.keys())
    if unique_cards == 1:
        return HAND_TYPES['5']
    if unique_cards == 2:
        # can both be 4 of a kind and Full house
        has_four = False
        for _, occurrences in card_map.items():
            if occurrences == 4:
                has_four = True
        if has_four:
            return HAND_TYPES['4']
        return HAND_TYPES['FH']
    if unique_cards == 3:
        # can be both three of a kind or two pair
        # 22334, 33345
        has_three = False
        for _, occurrences in card_map.items():
            if occurrences == 3:
                has_three = True
        if has_three:
            return HAND_TYPES['3']
        return HAND_TYPES['2']
    if unique_cards == 4:
        return HAND_TYPES['1']
    return HAND_TYPES['H']


def read_file(calculate_joker=False):
    f = open('input.txt')
    hands = []
    for line in f:
        cards, bid = line.split(' ')
        hands.append({
            'cards': cards,
            'bid': int(bid.strip()),
            'type': determine_hand_type(cards, calculate_joker)
        })
    f.close()
    return hands


def hand_lte(hand, other_hand):
    if hand['type'] != other_hand['type']:
        return hand['type'] <= other_hand['type']
    # same type, compare order of cards
    for i, card in enumerate(hand['cards']):
        if card != other_hand['cards'][i]:
            return POINTS[card] <= POINTS[other_hand['cards'][i]]


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if hand_lte(array[j], pivot):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


def part1():
    hands = read_file(False)
    my_hands = hands.copy()
    quicksort(my_hands, 0, len(my_hands) - 1)
    total_winnings = 0
    for i, hand in enumerate(my_hands):
        total_winnings += (i + 1) * hand['bid']
    print('part1', total_winnings)


def part2():
    hands = read_file(True)
    my_hands = hands.copy()
    POINTS['J'] = 1
    quicksort(my_hands, 0, len(my_hands) - 1)
    total_winnings = 0
    for i, hand in enumerate(my_hands):
        print(hand)
        total_winnings += (i + 1) * hand['bid']
    print('part2', total_winnings)


if __name__ == '__main__':
    part1()
    part2()

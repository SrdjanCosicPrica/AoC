f = open('input.txt')

tot = 0
tot_scratch_cards = 0
COPIES = {}


def increment_card_copy(index, amount):
  global tot_scratch_cards
  COPIES[index] = COPIES.get(index, 0) + amount
  tot_scratch_cards += amount


for i, line in enumerate(f):
  [card, numbers] = line.split(':')
  [winning_numbers, my_numbers] = numbers.split('|')
  winning_numbers = [number.strip() for number in winning_numbers.split(' ') if number]
  my_numbers = [number.strip() for number in my_numbers.split(' ') if number]

  increment_card_copy(i, 1)

  matches = [number for number in winning_numbers if number in my_numbers]
  if len(matches):
    tot += 2 ** (len(matches) - 1)
    for x in range(1, len(matches) + 1):
      increment_card_copy(i + x, COPIES[i])

print('part1', tot)
print('part2', tot_scratch_cards)

import re

SPELLED_NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_number(string):
  try:
    return int(string, 10)
  except:
    return SPELLED_NUMBERS.index(string) + 1

f = open('input.txt')

tot = 0
for line in f:
  # Lookahead assertion (?=(...))
  matches = re.findall(f"(?=(\d|{'|'.join(SPELLED_NUMBERS)}))", line)
  if matches:
    tot += int(f'{get_number(matches[0])}{get_number(matches[-1])}', 10)

print(tot)

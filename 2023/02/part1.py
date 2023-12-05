from enum import Enum

class Color(str, Enum):
  RED = "red"
  GREEN = "green"
  BLUE = "blue"

MAX_CUBES = { 
  Color.RED: 12,
  Color.GREEN: 13,
  Color.BLUE: 14
}

f = open('input.txt')

def get_default_occurrences():
  return {
    Color.RED: 0,
    Color.GREEN: 0,
    Color.BLUE: 0
  }

def get_cube_occurrences(cube_set):
  occurrences = get_default_occurrences()

  for cube in cube_set.split(','):
    [count, color] = cube.strip().split(' ')
    occurrences[color] = int(count)

  return occurrences

def compare_occurrences(current, new):
  calculated = {}
  for color in [Color.RED, Color.GREEN, Color.BLUE]:
    calculated[color] = max(current[color], new[color])
  return calculated

def is_game_possible(occurrences):
  for color in [Color.RED, Color.GREEN, Color.BLUE]:
    if (occurrences[color] > MAX_CUBES[color]):
      return False
  return True

sum_possible_games = 0

for line in f:
  [game, sets] = line.split(':')
  [_, game_number] = game.split(' ')
  
  max_occurrences = get_default_occurrences()
  for cube_set in sets.split(';'):
    set_occurrences = get_cube_occurrences(cube_set)
    max_occurrences = compare_occurrences(max_occurrences, set_occurrences)
  
  if is_game_possible(max_occurrences):
    sum_possible_games += int(game_number, 10)

print(sum_possible_games)

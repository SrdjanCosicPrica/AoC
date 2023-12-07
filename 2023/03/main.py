import re

f = open('input.txt')

matrix = [line for line in f]
LINE_LENGTH = len(matrix[0])


def get_line_and_neighbours(line_number):
    all_lines = []
    if line_number > 0:
        all_lines.append(matrix[line_number - 1])

    all_lines.append(matrix[line_number])

    if line_number < len(matrix) - 1:
        all_lines.append(matrix[line_number + 1])

    return all_lines


def get_span_bounds(match):
    start = match.start()
    end = match.end()

    if start > 0:
        start -= 1

    if end < LINE_LENGTH:
        end += 1

    return start, end


def is_regex_match_valid_number(match, line_number):
    for line in get_line_and_neighbours(line_number):
        start, end = get_span_bounds(match)

        # Search non word character, excluding "." and newline
        if re.search("(?!(\.|\n))\W", line[start:end]):
            return True
    return False


def get_gear(gear_match, line_number):
    found_numbers = []
    for line in get_line_and_neighbours(line_number):
        for number in re.finditer("\d+", line):
            if number.start() < gear_match.end() + 1 and number.end() > gear_match.start() - 1:
                found_numbers.append(int(number.group()))
    if len(found_numbers) == 2:
        return True, found_numbers[0] * found_numbers[1]
    return False, 0


tot = 0
total_gear_ratio = 0

for i, line in enumerate(matrix):
    for number in re.finditer("\d+", line):
        if is_regex_match_valid_number(number, i):
            tot += int(number.group())

    for possible_gear in re.finditer("\*", line):
        is_gear, ratio = get_gear(possible_gear, i)
        if is_gear:
            total_gear_ratio += ratio

print('part1', tot)
print('part2', total_gear_ratio)

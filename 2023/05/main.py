seeds = []
almanacs = []


def read_file():
    global seeds
    global almanacs
    f = open('input.txt')
    seeds = f.readline().strip().split('seeds: ')[1].split(' ')
    for line in f:
        if not line:
            continue

        if 'map:' in line:
            almanac = {'maps': []}
            for ranges in f:
                if not ranges.strip():
                    break

                [destination_start, source_start, _range] = ranges.strip().split(' ')
                source_start = int(source_start)
                destination_start = int(destination_start)
                _range = int(_range)
                almanac['maps'].append(
                    {
                        'source_start': source_start,
                        'destination_start': destination_start,
                        'range': _range
                    }
                )

            almanacs.append(almanac)

    f.close()


def get_seed_location(seed):
    global almanacs
    current_location = seed
    for almanac in almanacs:
        for _map in almanac['maps']:
            source_start = _map['source_start']
            destination_start = _map['destination_start']
            _range = _map['range']
            if source_start <= current_location <= source_start + _range:
                current_location = destination_start + (current_location - source_start)
                break
    return current_location


def part1():
    lowest_location = float('inf')
    for seed in seeds:
        seed = int(seed)
        seed_location = get_seed_location(seed)
        if seed_location < lowest_location:
            lowest_location = seed_location

    print('part1', lowest_location)


def get_destinations_for_almanac(almanac, range_start, range_end):
    destinations = []
    remaining_ranges = [[range_start, range_end]]
    for _map in almanac['maps']:
        map_destination_start = _map['destination_start']
        map_source_start = _map['source_start']
        map_range = _map['range']
        map_source_end = map_source_start + map_range

        next_remaining_ranges = []
        for start, end in remaining_ranges:
            left_start = min(start, map_source_start)
            left_end = min(end, map_source_start)
            if left_end - left_start > 0:
                next_remaining_ranges.append([left_start, left_end])

            overlap_start = max(start, map_source_start)
            overlap_end = min(end, map_source_end)
            if overlap_end - overlap_start > 0:
                start_index = overlap_start - map_source_start
                end_index = start_index + overlap_end - overlap_start
                destinations.append([
                    map_destination_start + start_index,
                    map_destination_start + end_index
                ])

            right_start = max(start, map_source_end)
            right_end = end
            if right_end - right_start > 0:
                next_remaining_ranges.append([right_start, right_end])

        remaining_ranges = next_remaining_ranges

    if remaining_ranges:
        destinations.extend(remaining_ranges)
    return destinations


def part2():
    global almanacs
    lowest_location = float('inf')
    for i in range(0, len(seeds), 2):
        seed_start, seed_length = int(seeds[i]), int(seeds[i + 1])
        seed_end = seed_start + seed_length

        viable_ranges = [(seed_start, seed_end)]
        for x, almanac in enumerate(almanacs):
            next_viable_ranges = []
            for range_start, range_end in viable_ranges:
                destinations = get_destinations_for_almanac(almanac, range_start, range_end)
                next_viable_ranges.extend(destinations)

            viable_ranges = next_viable_ranges
        for range_start, range_end in viable_ranges:
            if range_start < lowest_location:
                lowest_location = range_start

    print('part2', lowest_location)


if __name__ == '__main__':
    read_file()
    part1()
    part2()

races = []


def read_file():
    global races

    f = open('input.txt')
    times = [time for time in f.readline().split('Time:')[1].strip().split(' ') if
        time.strip()]
    distances = [
        distance for distance in f.readline().split('Distance:')[1].strip().split(' ')
        if distance.strip()
    ]

    for i, time in enumerate(times):
        races.append([time, distances[i]])

    f.close()


def get_number_of_ways(time, distance_to_beat):
    current_wind_up_time = time // 2
    while current_wind_up_time > 0:
        distance_per_ms = current_wind_up_time
        travel_time = time - current_wind_up_time
        if distance_per_ms * travel_time <= distance_to_beat:
            current_wind_up_time += 1
            break
        current_wind_up_time -= 1

    middle = time / 2
    return int((middle - current_wind_up_time) * 2 + 1)


def part1():
    global races
    product_number_of_ways = 1
    for time, distance_to_beat in races:
        number_of_ways = get_number_of_ways(int(time), int(distance_to_beat))
        if number_of_ways:
            product_number_of_ways *= number_of_ways

    print('part1', product_number_of_ways)


def part2():
    global races
    time = ''
    distance_to_beat = ''
    for race in races:
        time += race[0]
        distance_to_beat += race[1]

    time = int(time)
    distance_to_beat = int(distance_to_beat)
    print('part2', get_number_of_ways(time, distance_to_beat))


if __name__ == '__main__':
    read_file()
    part1()
    part2()

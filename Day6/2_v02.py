def calculate_max_distance(time, record):
    return sum(speed * (time - speed) > record for speed in range(time + 1))

with open('day6.txt') as file:
    time_value, distance_value = [int(''.join(line.split()[1:])) for line in file]

ways_to_win = calculate_max_distance(time_value, distance_value)
print(ways_to_win)

from functools import reduce
from operator import mul

def calculate_max_distance(time, record):
    return sum(speed * (time - speed) > record for speed in range(time + 1))

with open('day6.txt') as file:
    time_values, distance_values = [[int(val) for val in line.split()[1:]] for line in file]

total_ways_to_win = reduce(mul, (calculate_max_distance(time, record) for time, record in zip(time_values, distance_values)))
print(total_ways_to_win)
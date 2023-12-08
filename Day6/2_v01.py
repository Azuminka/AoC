def calculate_max_distance(time, record):
    a = 1
    b = -time
    c = record
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b - discriminant**0.5) / (2*a)
        root2 = (-b + discriminant**0.5) / (2*a)
        return max(0, int(root2) - int(root1) - 1)
    else:
        return 0

with open('day6.txt') as file:
    time_value, distance_value = [int(''.join(line.split()[1:])) for line in file]

ways_to_win = calculate_max_distance(time_value, distance_value)
print(ways_to_win)

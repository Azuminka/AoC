from itertools import islice
from itertools import cycle

input_data = open("day8.txt").readlines()
instructions = input_data[0].strip()
pointers_data = dict(line.strip().split(" = ") for line in islice(input_data, 2, None))
pointers_map = {address: tuple(pointer.strip("()\n").split(", ")) for address, pointer in pointers_data.items()}
get_next_address = lambda address, char: pointers_map[address][0 if char == 'L' else 1]
instruction_cycle = cycle(instructions)

current_address = "AAA"
steps = 0

for char in instruction_cycle:
    if current_address == "ZZZ":
        break
    current_address = get_next_address(current_address, char)
    steps += 1

print(steps)

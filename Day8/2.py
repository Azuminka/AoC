from math import lcm
from itertools import islice

def run_until_z(instructions, pointers_map, start_node):
    steps, current_node = 0, start_node
    while not current_node.endswith("Z"):
        current_node = pointers_map[current_node][instructions[steps % len(instructions)] == "R"]
        steps += 1
    return steps

input_data = open("day8.txt").readlines()
instructions = input_data[0].strip()
pointers_data = dict(line.strip().split(" = ") for line in islice(input_data, 2, None))
pointers_map = {address: tuple(pointer.strip("()\n").split(", ")) for address, pointer in pointers_data.items()}

steps_list = [run_until_z(instructions, pointers_map, node) for node in pointers_data if node.endswith("A")]
print(lcm(*steps_list))

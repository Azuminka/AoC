def parse_and_find_lowest_location(file_path):
    with open(file_path, 'r') as file:
        seeds = list(map(int, file.readline().split(': ')[1].split()))
        maps = {category: [] for category in ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 
                                             'water_to_light', 'light_to_temperature', 'temperature_to_humidity', 
                                             'humidity_to_location']}
        current_map = None
        for line in file:
            if 'map:' in line:
                current_map = maps[line.split(' map:')[0].replace('-', '_')]
            elif line.strip():
                current_map.append(list(map(int, line.split())))

    def map_number(number, mapping):
        for dest_start, src_start, length in mapping:
            if src_start <= number < src_start + length:
                return dest_start + (number - src_start)
        return number

    return min(map_number(map_number(map_number(map_number(map_number(map_number(map_number(seed, maps['seed_to_soil']), 
                                                                      maps['soil_to_fertilizer']), 
                                                          maps['fertilizer_to_water']), 
                                                  maps['water_to_light']), 
                                          maps['light_to_temperature']), 
                                  maps['temperature_to_humidity']), 
                      maps['humidity_to_location']) for seed in seeds)

lowest_location = parse_and_find_lowest_location('day5.txt')
print(lowest_location)

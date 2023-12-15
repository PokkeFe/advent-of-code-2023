FILENAME = "input.txt"

def get_group(file) -> list:
    group_almanac = []
    # Read the first line and ignore
    file.readline()
    for line in file:
        if line != '\n':
            group_almanac.append(line_to_map(line))
        else:
            break
    return group_almanac

def line_to_map(line : str) -> list:
    line = line.rstrip()
    string_values = line.split(' ')
    int_values = []
    for value in string_values:
        int_values.append(int(value))
    print(int_values)
    return int_values

def process_seed_through_map_group(seed, map_group):
    for map in map_group:
        step = map[2]
        # print("step: ", step)
        if (seed >= map[1]) and (seed <= map[1] + step-1):
            # print(" check: " ,check[0])
            return (seed - map[1] + map[0])
    return seed

def main():
    file = open(FILENAME, "r")

    # Load in seed inputs and convert
    seed_inputs = file.readline()[7:].rstrip().split(" ")
    for i in range(len(seed_inputs)):
        seed_inputs[i] = int(seed_inputs[i])
    print(seed_inputs)

    file.readline()
    all_maps = []
    group = get_group(file)
    while(len(group) > 0):
        all_maps.append(group)
        group = get_group(file)
    
    lowest_location_value = -1
    for seed in seed_inputs:
        # We have one seed. Pass it through all maps
        print("Seed: ", seed)
        value = seed
        for map_group in all_maps:
            value = process_seed_through_map_group(value, map_group)
        print(value, lowest_location_value)
        if lowest_location_value == -1:
            lowest_location_value = value
        elif value < lowest_location_value:
            lowest_location_value = value
    print(lowest_location_value)

main()
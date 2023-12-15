input_filename = "input.txt"


def get_game_power(game_string):
    cube_counts = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round_string in game_string.split("; "):
        round_cubes = round_string.split(", ")
        for cube_string in round_cubes:
            cube_count_str, cube_color = cube_string.split(" ")
            cube_count = int(cube_count_str)
            if(cube_counts[cube_color] < cube_count):
                cube_counts[cube_color] = cube_count
    game_power = 1
    for count in cube_counts.values():
        game_power *= count
    return game_power

def main():
    game_power_sum = 0

    file = open(input_filename, 'r')
    for line in file:
        line = line.strip()
        game_id_string, game_string = line.split(": ")
        game_power = get_game_power(game_string)
        game_power_sum += game_power
    
    print(game_power_sum)


main()
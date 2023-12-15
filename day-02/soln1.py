input_filename = "input.txt"

cube_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_round_valid(round_string):
    round_cubes = round_string.split(", ")
    for cube_string in round_cubes:
        cube_count, cube_color = cube_string.split(" ")
        if int(cube_count) > cube_limits[cube_color]:
            return False
    return True

def main():
    valid_game_ids_sum = 0

    file = open(input_filename, 'r')
    for line in file:
        line = line.strip()
        game_id_string, round_list_string = line.split(": ")
        game_id = int(game_id_string[5:])
        all_rounds_valid = True
        for round_string in round_list_string.split("; "):
            if not is_round_valid(round_string):
                all_rounds_valid = False
                break
        if all_rounds_valid:
            valid_game_ids_sum += game_id
    
    print(valid_game_ids_sum)


main()
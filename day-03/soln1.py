FILENAME = "input.txt"


def is_neighboring_symbol(lines : list[str], x : int, y : int) -> bool:
    if is_symbol(lines, x - 1, y - 1):
        return True
    if is_symbol(lines, x    , y - 1):
        return True
    if is_symbol(lines, x + 1, y - 1):
        return True
    
    if is_symbol(lines, x - 1, y    ):
        return True
    
    # This is where the origin would be :)

    if is_symbol(lines, x + 1, y    ):
        return True
    
    if is_symbol(lines, x - 1, y + 1):
        return True
    if is_symbol(lines, x    , y + 1):
        return True
    if is_symbol(lines, x + 1, y + 1):
        return True
    return False

def is_symbol(lines : list[str], x : int, y : int):
    if not is_in_bounds(lines, x, y):
        return False
    ch = lines[y][x]
    if ch.isnumeric():
        return False
    if ch == "." or ch == "\n":
        return False
    return True

def is_in_bounds(lines : list[str], x : int, y : int):
    if x < 0 or y < 0:
        return False
    if y >= len(lines) or x >= len(lines[y]):
        return False
    return True
    

def main():
    file = open(FILENAME, "r")
    lines = file.readlines()

    total_sum = 0
    number_string = ""

    for y in range(len(lines)):
        number_string = ""
        neighboring_symbol = False
        in_number_string = False

        for x in range(len(lines[y])):
            ch = lines[y][x]
            if ch.isnumeric():
                number_string += ch
                if is_neighboring_symbol(lines, x, y):
                    neighboring_symbol = True
                in_number_string = True
            else:
                if in_number_string:
                    if neighboring_symbol:
                        total_sum += int(number_string)
                    print(y, ": ", total_sum, " - ", int(number_string))
                    number_string = ""
                    in_number_string = False
                    neighboring_symbol = False
            
        if in_number_string:
            if neighboring_symbol:
                total_sum += int(number_string)
                print(y, ": ", total_sum, " - ", int(number_string))
            number_string = ""
            in_number_string = False
            neighboring_symbol = False
    
    print(total_sum)


main()
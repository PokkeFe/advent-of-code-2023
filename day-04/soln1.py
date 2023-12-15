FILENAME = "input.txt"

def main():
    file = open(FILENAME, "r")

    total_sum = 0

    for line in file:
        # Split the card number from the sets
        split_line = line.split(": ")

        card_number = split_line[0][5:]
        card_value = 0

        # Split the sets into guess and winning
        win_set_string, guess_set_string = split_line[1].split(" | ")

        # Split both sets by spaces to get individual elements
        win_set = win_set_string.replace("  ", " ").strip().split(" ")
        guess_set = guess_set_string.replace("  ", " ").strip().split(" ")

        # Loop over each guess and check if it's in winning number
        # If it is, double the card point score (or set to 1 if its the first one)
        for guess in guess_set:
            if win_set.__contains__(guess):
                if card_value == 0:
                    card_value = 1
                else:
                    card_value = card_value * 2
        # Add card value to sum
        total_sum += card_value
    print(total_sum)

main()
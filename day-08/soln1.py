filename = "input.txt"

network = {}

def add_line_to_network(line):
    key, value = line.split(" = ")
    left, right = value[1:-2].split(", ")
    network[key] = (left, right)

def main():
    file = open(filename, "r")
    instruction = file.readline()
    file.readline()
    for line in file:
        add_line_to_network(line)
    # Network has been loaded into memory. Let's start stepping through.
    step = 0
    active_element = 'AAA'
    while active_element != 'ZZZ':
        direction = instruction[step % (len(instruction) - 1)]
        if direction == 'L':
            active_element = network[active_element][0]
        else:
            active_element = network[active_element][1]
        step += 1
    print(step)

main()
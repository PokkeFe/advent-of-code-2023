import math

filename = "input.txt"

network = {}

active_nodes = []

def add_line_to_network(line):
    key, value = line.split(" = ")
    left, right = value[1:-2].split(", ")
    network[key] = (left, right)
    if key[2] == 'A':
        active_nodes.append(key)

def all_complete(lcm_tracker):
    for node_info in lcm_tracker.values():
        if not node_info["complete"]:
            return False
    return True

def is_solved(node_info):
    if node_info["current_node"][2] != 'Z':
        return False
    return True

def main():
    global active_nodes
    file = open(filename, "r")
    instruction = file.readline()
    file.readline()
    for line in file:
        add_line_to_network(line)
    # Network has been loaded into memory. Let's build our data struct
    lcm_tracker = {}
    for node in active_nodes:
        lcm_tracker[node] = {
            "start_nodes": [node],
            "steps": 0,
            "current_node": node,
            "steps_to_z": 0,
            "complete": False,
        }
    step = 0
    while not all_complete(lcm_tracker):
        instruction_index = step % (len(instruction) - 1)
        direction = instruction[instruction_index]
        # double buffer that bad boy
        for node_info in lcm_tracker.values():
            if not node_info["complete"]:
                current_node = node_info["current_node"]
                if direction == 'L':
                    node_info["current_node"] = network[current_node][0]
                else:
                    node_info["current_node"] = network[current_node][1]
            if is_solved(node_info):
                node_info["steps_to_z"] = step + 1
        step += 1
        # If we've looped through all instructions, check to see if we've made it back to the origin
        if (step % (len(instruction) - 1)) == 0:
            for node_info in lcm_tracker.values():
                if node_info["complete"] == False:
                    if node_info["current_node"] in node_info["start_nodes"]:
                        node_info["complete"] = True
                        node_info["steps"] = step
                    node_info["start_nodes"].append(node_info["current_node"])
    # All complete. Let's figure out LCM
    integers = []
    for node_info in lcm_tracker.values():
        integers.append(node_info["steps_to_z"])
    print(math.lcm(*integers))

main()
def navigate_network(instructions, start_node='AAA', end_node='ZZZ'):
    # Parse the input to create a dictionary representing the network
    network = {}
    for line in instructions:
        node, connections = line.split(' = ')
        network[node] = tuple(connections.split(', '))

    current_node = start_node
    steps = 0

    for instruction in instructions:
        direction = instruction[0]
        current_node = network[current_node][1] if direction == 'R' else network[current_node][0]
        steps += 1

        if current_node == end_node:
            return steps

    return steps

if __name__ == "__main__" :
    instructions = "LLR"
    steps_to_ZZZ = navigate_network(instructions)
    print(f"Steps required to reach ZZZ: {steps_to_ZZZ}")

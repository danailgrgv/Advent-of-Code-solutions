f = open("input.txt", "r")
input = f.read()
instructions = input.splitlines()
f.close()

# wire 'a' in original task
TARGET_WIRE_PART_1 = 'a'
TARGET_WIRE_PART_2 = 'b'
wires = []
wire_values = []

# checks if a string is a wire or a value
def is_wire(data):
    is_wire = False
    try:
        int_data = int(data)
    except:
        is_wire = True
    else:
        is_wire = False
    
    return is_wire

# gets the value of a wire (-1 if not yet acquired)
def get_wire_value(wire):
    return wire_values[wires.index(wire)]

# sets the value of a wire
def set_wire_value(wire, wire_value):
    wire_values[wires.index(wire)] = int(wire_value)

# gets the direct instructions for calculating the value of a wire
def get_wire_instruction(wire):
    wire_instruction = ''
    for instruction in instructions:
        right_side = instruction.split(" -> ")[1]
        if(wire == right_side):
            wire_instruction = instruction.split(" -> ")[0]
    return wire_instruction

# manually set a wire's instructions
def set_wire_instruction(wire, new_instruction):
    new_instruction = str(new_instruction)
    for i, instruction in enumerate(instructions):
        right_side = instruction.split(" -> ")[1]
        if(wire == right_side):
            instructions[i] = new_instruction + " -> " + right_side


def solve_NOT_gate(source):
    result = 65535 - solve_wire(source)
    return result

def solve_OR_gate(source_A, source_B):
    result = solve_wire(source_A) | solve_wire(source_B)
    return result

def solve_AND_gate(source_A, source_B):
    result = solve_wire(source_A) & solve_wire(source_B)
    return result

def solve_LSHIFT_gate(source_A, source_B):
    result = solve_wire(source_A) << solve_wire(source_B)
    return result

def solve_RSHIFT_gate(source_A, source_B):
    result = solve_wire(source_A) >> solve_wire(source_B)
    return result

# recursively follow the instructions to solve a wire, down to the raw values
def solve_wire(wire):
    # check if the wire is actually a solved signal
    if(not is_wire(wire)):
        return int(wire)
    
    instruction = get_wire_instruction(wire)
    
    # check if already solved
    wire_value = get_wire_value(wire)
    if(wire_value != -1):
        return wire_value
    
    # parse the left side
    if("NOT" in instruction):
        source = instruction.split("NOT ")[1]
        wire_value = solve_NOT_gate(source)
    elif("OR" in instruction):
        sources = instruction.split(" OR ")
        wire_value = solve_OR_gate(sources[0], sources[1])
    elif("AND" in instruction):
        sources = instruction.split(" AND ")
        wire_value = solve_AND_gate(sources[0], sources[1])
    elif("LSHIFT" in instruction):
        sources = instruction.split(" LSHIFT ")
        wire_value = solve_LSHIFT_gate(sources[0], sources[1])
    elif("RSHIFT" in instruction):
        sources = instruction.split(" RSHIFT ")
        wire_value = solve_RSHIFT_gate(sources[0], sources[1])
    else:
        if(not is_wire(instruction)):
            wire_value = int(instruction)
        else:
            wire_value = solve_wire(instruction)

    # set the wire values
    set_wire_value(wire, wire_value)
    return int(wire_value)

# get all wires
for instruction in instructions:
    split_instruction = instruction.split(" -> ")
    left_side = split_instruction[0]
    right_side = split_instruction[1]
    if (right_side not in wires) and is_wire(right_side):
        wires.append(right_side)

# initialize wire_values array with invalid values
wire_count = len(wires)
wire_values = [-1 for i in range(wire_count)]

result = solve_wire(TARGET_WIRE_PART_1)
print("target wire (part 1) ", TARGET_WIRE_PART_1, " = ", result)

# Part 2

# reset the wire values
wire_values = [-1 for i in range(wire_count)]

# override the signal to the new target wire to be the result from Part 1
set_wire_instruction(TARGET_WIRE_PART_2, result)
result = solve_wire(TARGET_WIRE_PART_1)
print("target wire (part 2) ", TARGET_WIRE_PART_1, " = ", result)
f = open("input.txt", "r")
input = f.read()
instructions = input.splitlines()
f.close()

lights = [[0 for col in range(1000)] for row in range(1000)]

# turn on a light at a coordinate
def turn_on_light_part_1(coordinate):
    lights[coordinate[0]][coordinate[1]] = 1

# turn off a light at a coordinate
def turn_off_light_part_1(coordinate):
    lights[coordinate[0]][coordinate[1]] = 0

# turn light on if off, or off if on at a coordinate
def toggle_light_part_1(coordinate):
    if(lights[coordinate[0]][coordinate[1]] == 1):
        lights[coordinate[0]][coordinate[1]] = 0
    else:
        lights[coordinate[0]][coordinate[1]] = 1

# execute an instruction for a range of lights with part 1 rules
def execute_instruction_part_1(instruction):
    split_line = instruction.split(' ')
    coordinate_end_string = split_line[len(split_line) - 1]
    coordinate_end = coordinate_end_string.split(',')
    if("turn on" in instruction):
        coordinate_start_string = split_line[2]
        coordinate_start = coordinate_start_string.split(',')
        x = int(coordinate_start[0])
        y = int(coordinate_start[1])
        while x <= int(coordinate_end[0]):
            while y <= int(coordinate_end[1]):
                turn_on_light_part_1([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    elif("turn off" in instruction):
        coordinate_start_string = split_line[2]
        coordinate_start = coordinate_start_string.split(',')
        x = int(coordinate_start[0])
        y = int(coordinate_start[1])
        while x <= int(coordinate_end[0]):
            while y <= int(coordinate_end[1]):
                turn_off_light_part_1([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    elif("toggle" in instruction):
        coordinate_start_string = split_line[1]
        coordinate_start = coordinate_start_string.split(',')
        x = int(coordinate_start[0])
        y = int(coordinate_start[1])
        while x <= int(coordinate_end[0]):
            while y <= int(coordinate_end[1]):
                toggle_light_part_1([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    else:
        print("invalid instruction!")

for instruction in instructions:
    execute_instruction_part_1(instruction)

total_lights_on = 0
for row in lights:
    total_lights_on += sum(row)
print("Part 1: total lights on = ", total_lights_on)

lights = [[0 for col in range(1000)] for row in range(1000)]

# Part 2

# increase brightness at a coordinate
def turn_on_light_part_2(coordinate):
    lights[coordinate[0]][coordinate[1]] += 1

# decrease brightness at a coordinate
def turn_off_light_part_2(coordinate):
    lights[coordinate[0]][coordinate[1]] -= 1
    if(lights[coordinate[0]][coordinate[1]] < 0):
        lights[coordinate[0]][coordinate[1]] = 0

# increase brightness at a coordinate with 2
def toggle_light_part_2(coordinate):
    lights[coordinate[0]][coordinate[1]] += 2

# execute an instruction for a range of lights with part 2 rules
def execute_instruction_part_2(instruction):
    split_line = instruction.split(' ')
    coordinate_end_string = split_line[len(split_line) - 1]
    coordinate_end = coordinate_end_string.split(',')
    if("turn on" in instruction):
        coordinate_start_string = split_line[2]
        coordinate_start = coordinate_start_string.split(',')
        x = int(coordinate_start[0])
        y = int(coordinate_start[1])
        while x <= int(coordinate_end[0]):
            while y <= int(coordinate_end[1]):
                turn_on_light_part_2([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    elif("turn off" in instruction):
        coordinate_start_string = split_line[2]
        coordinate_start = coordinate_start_string.split(',')
        x = int(coordinate_start[0])
        y = int(coordinate_start[1])
        while x <= int(coordinate_end[0]):
            while y <= int(coordinate_end[1]):
                turn_off_light_part_2([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    elif("toggle" in instruction):
        coordinate_start_string = split_line[1]
        coordinate_start = coordinate_start_string.split(',')
        x = int(coordinate_start[0])
        y = int(coordinate_start[1])
        while x <= int(coordinate_end[0]):
            while y <= int(coordinate_end[1]):
                toggle_light_part_2([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    else:
        print("invalid instruction!")

for instruction in instructions:
    execute_instruction_part_2(instruction)

total_lights_brightness = 0
for row in lights:
    total_lights_brightness += sum(row)
print("Part 2: total lights brightness = ", total_lights_brightness)
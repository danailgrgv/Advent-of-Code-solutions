f = open("input.txt", "r")
input = f.read()
lines = input.splitlines()
f.close()
lights = [[0 for col in range(1000)] for row in range(1000)]

def turn_on_light(coordinate):
    lights[coordinate[0]][coordinate[1]] += 1

def turn_off_light(coordinate):
    lights[coordinate[0]][coordinate[1]] -= 1
    if(lights[coordinate[0]][coordinate[1]] < 0):
        lights[coordinate[0]][coordinate[1]] = 0

def toggle_light(coordinate):
    lights[coordinate[0]][coordinate[1]] += 2

def execute_instruction(instruction):
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
                turn_on_light([x, y])
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
                turn_off_light([x, y])
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
                toggle_light([x, y])
                y += 1
            y = int(coordinate_start[1])
            x += 1
    else:
        print("invalid instruction!")

for line in lines:
    execute_instruction(line)

total_lights_on = 0
for row in lights:
    total_lights_on += sum(row)
print(total_lights_on)


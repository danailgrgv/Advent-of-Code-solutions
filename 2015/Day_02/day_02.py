f = open("input.txt", "r")
instructions = f.read()
f.close()
instructions = instructions.splitlines()

# Part 1: get the area of the necessary wrapping paper
total_area = 0
for instruction in instructions:
    box_dimentions = instruction.split("x")
    length = int(box_dimentions[0])
    width = int(box_dimentions[1])
    height = int(box_dimentions[2])
    side_areas = [length * width, width * height, height * length]
    total_area += 2 * sum(side_areas) + min(side_areas)

print("Total wrapping paper = ", total_area)

# Part 2: calculate the necessary ribbon length
ribbon_length = 0
for instruction in instructions:
    box_dimentions = instruction.split("x")
    length = int(box_dimentions[0])
    width = int(box_dimentions[1])
    height = int(box_dimentions[2])
    sides = [length, width, height]
    ribbon_length += 2 * sum(sorted(sides)[:2]) + (length * width * height)

print("Total ribbon length = ", ribbon_length)
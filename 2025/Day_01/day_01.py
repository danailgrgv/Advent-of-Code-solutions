f = open("input.txt", "r")
input = f.read()
instructions = input.splitlines()
f.close()

location = 50
counter = 0

# Part 1

for i, instruction in enumerate(instructions):
    counts = 0
    if "L" in instruction:
        counts = int(instruction.split("L")[1])
        index = -1

        while(counts > 0):
            location -= 1
            counts -= 1
            if(location == -1):
                location = 99
    else:
        counts = int(instruction.split("R")[1])
        index = 1
        while(counts > 0):
            location += 1
            counts -= 1
            if(location == 100):
                location = 0
            
    if(location == 0):
        counter += 1

print("Counts of 0 (Part 1) = ", counter)

# Part 2

counter = 0
for i, instruction in enumerate(instructions):
    counts = 0
    if "L" in instruction:
        counts = int(instruction.split("L")[1])
        index = -1

        while(counts > 0):
            location -= 1
            counts -= 1
            if(location == -1):
                location = 99
            
            if(location == 0):
                counter += 1
    else:
        counts = int(instruction.split("R")[1])
        index = 1
        while(counts > 0):
            location += 1
            counts -= 1
            if(location == 100):
                location = 0
            
            if(location == 0):
                counter += 1

print("Counts of 0 (Part 2) = ", counter)
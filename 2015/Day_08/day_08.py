f = open("input.txt", "r")
input = f.read()
input = input.splitlines()
f.close()

in_code_sum = 0
in_memory_sum = 0

for line in input:
    # calculate the memory
    index = 0
    length = len(line)

    memory_counter = 0
    while index < length:
        if(line[index] == '\\'):
            if(line[index+1] == '\\'):
                memory_counter += 1
                index += 2
            elif(line[index+1] == '\"'):
                memory_counter += 1
                index += 2
            elif(line[index+1] == 'x'):
                memory_counter += 1
                index += 4
        else:
            memory_counter += 1
            index += 1

    # account for the opening and closing quotes
    memory_counter -= 2

    in_memory_sum += memory_counter
    in_code_sum += len(line)  

print("Difference (Part 1) = ", in_code_sum - in_memory_sum)

# Part 2
extrachars = 0

for line in input:
    counter = 2
    for char in line:
        if char == '\\' or char == '\"':
            counter += 1

    extrachars += counter

print("Difference (Part 2) = ", extrachars)
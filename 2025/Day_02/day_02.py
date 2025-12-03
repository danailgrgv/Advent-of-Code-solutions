f = open("input.txt", "r")
instructions = f.read()
ranges = instructions.split(",")
f.close()

ranges_left = []
ranges_right = []

for range in ranges:
    numbers = range.split('-')
    ranges_left.append(int(numbers[0]))
    ranges_right.append(int(numbers[1]))

# Part 1

# checks if an ID is invalid acording to part 1 rules, returns it if so, else 0
def check_if_valid_part_1(id):
    id_str = str(id)
    length = len(id_str)

    # if odd number of digits, it's valid
    if(length % 2 != 0):
        return 0
    
    half_length = int(length/2)
    index = 0

    while index < half_length:
        if(id_str[index] != id_str[index + half_length]):
            return 0
        index += 1
        
    return id

# check a range for invalid IDs, returns the sum
def check_range_part_1(start, end):
    id_sum = 0
    id = start

    while id <= end:
        id_sum += check_if_valid_part_1(id)
        id += 1

    return id_sum

total_sum = 0

for i, range in enumerate(ranges):
    invalid_id_sum = check_range_part_1(ranges_left[i], ranges_right[i])
    total_sum += invalid_id_sum

print("total sum Part 1 = ", total_sum)

# Part 2

# check if an id is mate only of a repeating pattern
def check_for_pattern(id, pattern):
    count = len(id.split(pattern))- 1
    for elem in id.split(pattern):
        if elem != '':
            return False
    if(count > 1):
        return True
    return False

# checks if an ID is invalid acording to part 2 rules, returns it if so, else 0
def check_if_valid_part_2(id):
    id_str = str(id)
    length = len(id_str)

    index = 0
    patterns = []

    # get all possible patterns
    while index < length - 1:
        reverse_index = length - 1
        while(reverse_index > index):
            pattern = id_str[index:reverse_index]
            patterns.append(pattern)
            reverse_index -= 1
        index += 1
    
    # check for each pattern
    for pattern in patterns:
        if(check_for_pattern(id_str, pattern) == True):
            return (id)
        
    return 0

# check a range for invalid IDs, returns the sum
def check_range_part_2(start, end):
    id_sum = 0
    id = start

    while id <= end:
        id_sum += check_if_valid_part_2(id)
        id += 1

    return id_sum

total_sum = 0

for i, range in enumerate(ranges):
    invalid_id_sum = check_range_part_2(ranges_left[i], ranges_right[i])
    total_sum += invalid_id_sum

print("total sum Part 2 = ", total_sum)
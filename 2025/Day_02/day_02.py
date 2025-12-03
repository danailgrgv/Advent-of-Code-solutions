def check_for_pattern(id, pattern):
    count = len(id.split(pattern))- 1
    for elem in id.split(pattern):
        if elem != '':
            return False
    if(count > 1):
        return True
    return False

def check_valid(id):
    length = len(str(id))
    id = str(id)
    index = 0
    patterns = []

    while index < length - 1:
        reverse_index = length - 1
        while(reverse_index > index):
            pattern = id[index:reverse_index]
            patterns.append(pattern)
            reverse_index -= 1
        index += 1
    

    for pattern in patterns:
        if(check_for_pattern(id, pattern) == True):
            return (int(id))
        
    return 0

def check_range(start, end):
    added = 0
    id = start

    while id <= end:
        added += check_valid(id)
        id += 1

    return added

f = open("input.txt", "r")
instructions = f.read()

ranges = instructions.split(",")

ranges_left = []
ranges_right = []

for range in ranges:
    numbers = range.split('-')
    ranges_left.append(int(numbers[0]))
    ranges_right.append(int(numbers[1]))

total_sum = 0

for i, range in enumerate(ranges):
    invalid_id_sum = check_range(ranges_left[i], ranges_right[i])
    total_sum += invalid_id_sum

print("total_sum = ", total_sum)

f.close()
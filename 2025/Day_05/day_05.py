f = open("input.txt", "r")
input = f.read()
lines = input.splitlines()
f.close()

ranges = []
ingredients = []
reading_ranges = True

for line in lines:
    if(line == ''):
        reading_ranges = False
        continue
    if(reading_ranges):
        ranges.append(line)
    else:
        ingredients.append(int(line))

print(ranges)
print(ingredients)

# get range as a 2-length array
def get_range(range_str):
    range_arr = []
    range_arr.append(int((range_str.split('-')[0])))
    range_arr.append(int((range_str.split('-')[1])))
    return range_arr

# checks if an ingredient is in any of the ranges
def is_fresh(ingredient, ranges):
    for range_str in ranges:
        range_arr = get_range(range_str)
        if(ingredient >= range_arr[0]) and (ingredient <= range_arr[1]):
            return True
    return False

# go through all the ingredients and count the fresh ones
fresh_counter = 0
for ingredient in ingredients:
    if(is_fresh(ingredient, ranges)):
        fresh_counter += 1

print("Total number of fresh ingredients: ", fresh_counter)

# check if 2 ranges are overlapping
def are_overlapping(range_str_1, range_str_2):
        range_arr_1 = get_range(range_str_1)
        range_arr_2 = get_range(range_str_2)

        # Check if first range starts before second
        if(range_arr_1[0] <= range_arr_2[0]):
            # Check if second range starts before first ends
            if(range_arr_2[0] <= range_arr_1[1]):
                return(True)
        # Check if second range starts before first
        if(range_arr_2[0] <= range_arr_1[0]):
            # Check if first range starts before second ends
            if(range_arr_1[0] <= range_arr_2[1]):
                return(True)
        return(False)

# explicit, no?
def get_number_of_valid_IDs_in_range(range_str):
    if(range_str == ''):
        return 0
    range_arr = get_range(range_str)
    return (range_arr[1] - range_arr[0] + 1)

# finds a pair of overlapping ranges and joins them
# returns True if it joined any ranges, 0 if none
def find_and_join_ranges(ranges):
    for i, range_str_1 in enumerate(ranges):
        if(range_str_1 == ''):
            continue
        for j, range_str_2 in enumerate(ranges):
            if(range_str_2 == ''):
                continue
            if(i == j):
                continue
            if(are_overlapping(range_str_1, range_str_2)):
                range_arr_1 = get_range(range_str_1)
                range_arr_2 = get_range(range_str_2)

                if(range_arr_1[0] <= range_arr_2[0]):
                    start = str(range_arr_1[0])
                else:
                    start = str(range_arr_2[0])

                if(range_arr_1[1] <= range_arr_2[1]):
                    end = str(range_arr_2[1])
                else:
                    end = str(range_arr_1[1])

                new_range_str = start + '-' + end
                ranges[i] = new_range_str
                ranges[j] = ''
                return True
            
    return False

# keep going until all overlapping ranges are merged
while(find_and_join_ranges(ranges)): pass

fresh_ID_counter = 0
for range in ranges:
    fresh_ID_counter += get_number_of_valid_IDs_in_range(range)

print("Total number of fresh IDs: ", fresh_ID_counter)
f = open("input.txt", "r")
instructions = f.read()
f.close()

# start at ground floor
floor = 0

BASEMENT = -1
first_entry = 0
went_to_basement = False

# Part 1: Calculate the final floor
for i, elem in enumerate(instructions):
    if elem == '(':
        floor += 1
    elif elem == ')':
        floor -= 1
    # Part 2: Get the first entry of basement
    if floor == BASEMENT and not went_to_basement:
        first_entry = i + 1
        went_to_basement = True

print("Final floor: ", floor)
print("First basement entry at position: ", first_entry)
f = open("input.txt", "r")
instructions = f.read()
f.close()

# Part 1
locations = []
current_location = [0, 0]
locations.append(current_location.copy())

# Check if the location has already been visited
def check_if_visited(current_location, visited_locations):
    for location in visited_locations:
        if location == current_location:
            return True
    return False
    
for direction in instructions:
    new_location = current_location.copy()
    if direction == '^':
        new_location[1] += 1
    elif direction == 'v':  
        new_location[1] -= 1
    elif direction == '<':
        new_location[0] -= 1
    elif direction == '>':
        new_location[0] += 1
    
    # Add the location to the list if not visited before
    if(check_if_visited(new_location, locations) == False):
        locations.append(new_location.copy())

    current_location = new_location

print(f"Unique locations: {len(locations)}")

# Part 2
locations = []
santa_location = [0, 0]
robo_santa_location = [0, 0]

santa_to_move = True

locations.append(santa_location.copy())

for instruction in instructions:
    if(santa_to_move):
        new_location = santa_location.copy()
    else:
        new_location = robo_santa_location.copy()

    if instruction == '^':
        new_location[1] += 1
    elif instruction == 'v':  
        new_location[1] -= 1
    elif instruction == '<':
        new_location[0] -= 1
    elif instruction == '>':
        new_location[0] += 1

    if(check_if_visited(new_location, locations) == False):
        locations.append(new_location.copy())
    
    if(santa_to_move):
        santa_location = new_location.copy()
        santa_to_move = False
    else:
        robo_santa_location = new_location.copy()
        santa_to_move = True

print(f"Unique locations: {len(locations)}")


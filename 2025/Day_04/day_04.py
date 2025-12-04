f = open("input.txt", "r")
input = f.read()
grid = input.splitlines()
f.close()

# convert the grid from strings to char arrays
char_grid = []
for row in grid:
    char_row = []
    for cell in row:
        char_row.append(cell)
    char_grid.append(char_row)
grid = char_grid

row_count = len(grid)
column_count = len(grid[0])

# check if a roll is accessible according to the rules
def is_accessable(x, y):
    neighbour_counter = 0

    # top row
    if(x > 0):
        # above
        if(grid[x-1][y] == '@'):
            neighbour_counter += 1
         # above left
        if(y > 0):
            if(grid[x-1][y-1] == '@'):
                neighbour_counter += 1
        # above right    
        if(y < column_count - 1):
            if(grid[x-1][y+1] == '@'):
                neighbour_counter += 1

    # middle row
    # left
    if(y > 0):
        if(grid[x][y-1] == '@'):
                neighbour_counter += 1
    # right
    if(y < column_count - 1):
        if(grid[x][y+1] == '@'):
                neighbour_counter += 1

    # row below
    if(x < row_count - 1):
        # below
        if(grid[x+1][y] == '@'):
            neighbour_counter += 1
        # below left
        if(y > 0):
            if(grid[x+1][y-1] == '@'):
                neighbour_counter += 1
        # below right    
        if(y < column_count - 1):
            if(grid[x+1][y+1] == '@'):
                neighbour_counter += 1

    if(neighbour_counter < 4):
        return True
    else:
        return False

counter = 0
for x, row in enumerate(grid):
    for y, cell in enumerate(row):
        if(cell == '@'):
            counter += is_accessable(x, y)

print("Accessible rolls = ", counter)

# part 2

# removes all rolls marked with 'x', returns the number of rolls removed
def remove_rolls(grid):
    rm_counter = 0
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == 'x':
                grid[x][y] = '.'
                rm_counter += 1
    return rm_counter

# scan removable rolls and mark them with 'x'
def scan_removable(grid):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if(cell == '@'):
                if(is_accessable(x, y)):
                    row[y] = 'x'

rm_counter = 0
while(True):
    scan_removable(grid)
    removed_count = remove_rolls(grid)
    if(removed_count == 0):
        break
    rm_counter += removed_count

print("Could remove = ", rm_counter)
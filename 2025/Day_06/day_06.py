f = open("input.txt", "r")
input = f.read()
lines_str = input.splitlines()
f.close()

lines = []

for i, line_str in enumerate(lines_str):
    # if it's come to the operators line, break the loop and read it differently
    if i == len(lines_str) - 1:
        break
    line = []
    numbers_str = line_str.split(' ')
    for number_str in numbers_str:
        if(not number_str.isspace() and number_str != ''):
            number = int(number_str.strip())
            line.append(number)
    lines.append(line)

# read the operators
operators = []
for operator in lines_str[-1]:
    if(not operator.isspace()):
        to_add = operator.strip()
        operators.append(to_add)

# Do the calculations
results = []
for i, operator in enumerate(operators):
    # get the numbers
    numbers = []
    for line in lines:
        numbers.append(line[i])

    if(operator == '+'):
        result = sum(numbers)
    elif(operator == '*'):
        result = 1
        for number in numbers:
            result *= number
    results.append(result)

total = sum(results)
print("Sum of results of calculations = ", total)

# Part 2

# convert input into char arrays to enable manipulation
char_lines = []
for line in lines_str:
    char_line = list(line)
    char_lines.append(char_line)

# facilitate the splitting by replacing the empty columns with 'X' columns
for i, char in enumerate(char_lines[0]):
    is_separator = True
    for char_line in char_lines:
        if(char_line[i] != ' '):
            is_separator = False
            break
    if(is_separator):
        for char_line in char_lines:
            char_line[i] = 'X'

# convert back to strings for easier splitting
string_lines = []
for char_line in char_lines:
    string_line = ""
    for char in char_line:
        string_line += char
    string_lines.append(string_line)

# split
split_string_lines = []
for string_line in string_lines:
    split_string_line = string_line.split('X')
    split_string_lines.append(split_string_line)

# divide into problem lists
problems_strings = []
for i, problem_line in enumerate(split_string_lines[0]):
    problem = []
    for split_string_line in split_string_lines:
        problem.append(split_string_line[i])
    problems_strings.append(problem)

# get the operator of the problem, + or *
def get_operator(problem):
    return problem[-1].strip()

# returns the result of the problem when solved
def solve_problem(problem):
    numbers = []
    for i, char in enumerate(problem[0]):
        number = ''
        for line in problem[:-1]:
            number += line[i]
        numbers.append(int((number.strip())))

    print(numbers)

    operator = get_operator(problem)
    if(operator == '*'):
        result = 1
        for number in numbers:
            result *= number
    elif operator == '+':
        result = sum(numbers)
    return result

total = 0

# go through all problems and sum the results
for problem in problems_strings:
    result = solve_problem(problem)
    total += result

print("Part 2 total = ", total)
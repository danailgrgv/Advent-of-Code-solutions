# Part 1

VOWELS = "aeiou"
BAD_STRINGS = ["ab", "cd", "pq", "xy"]

# checks a string for having at least three vowels
def check_for_three_vowels(string_input):
    vowel_counter = 0

    for letter in string_input:
        if(letter in VOWELS):
            vowel_counter += 1
    
    if(vowel_counter >= 3):
        return True
    return False

# checks a string if it contains a letter that repeats consecutively
def check_for_twice_in_a_row(string_input):
    for i, letter in enumerate(string_input):
        # end of string
        if(i == len(string_input) - 1):
            return False
        if letter == string_input[i+1]:
            return True
    return False

# checks if the string contains any of the "bad" strings
def check_for_no_bad_strings(string_input):
    for bad_string in BAD_STRINGS:
        if(bad_string in string_input):
            return False
    return True

# checks a string if it adheres to all three rules
def is_nice_part_one(string_input):
    return(check_for_three_vowels(string_input) and check_for_twice_in_a_row(string_input) and check_for_no_bad_strings(string_input))

f = open("input.txt", "r")
instructions = f.read()
strings = instructions.splitlines()
f.close()

counter = 0

for string in strings:
    if(is_nice_part_one(string)):
        counter+=1

print("nice strings (part 1) = ", counter)

# Part 2

# checks if a pair of letters repeats in the string
def rule_one(string_input):
    for index, letter in enumerate(string_input):
        # check for end of string
        if(index >= len(string_input) - 1):
            return False
        # take a pair of digits
        pair = letter + string_input[index + 1]
        # check the remainder of the string for a repetition of this pair
        if(pair in string_input[index + 2:]):
            return True

# checks if at least one letter repeats with exactly 1 letter inbetween them
def rule_two(string_input):
    for index, letter in enumerate(string_input):
        # checks for end of string
        if(index >= len(string_input) - 2):
            return False
        # checks the letter 1 over if its the same
        if(string_input[index + 2] == letter):
            return True

# checks the string if it adheres to both rules
def is_nice_part_two(string_input):
    if(rule_one(string_input) and rule_two(string_input)):
        return True
    else:
        return False
    
counter = 0

for string in strings:
    if(is_nice_part_two(string)):
        counter+=1

print("nice strings (part 2) = ", counter)
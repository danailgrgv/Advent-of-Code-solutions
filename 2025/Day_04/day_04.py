import hashlib

f = open("input.txt", "r")
key = f.read()
f.close()

def hash(data, key):
    string_to_hash = str(key) + str(data)
    hashedVal = hashlib.md5(string_to_hash.encode()).hexdigest()
    return hashedVal

# Check if the hash starts with five 0s
def check_if_correct_part_1(hash):
    if(hash[:5] == "00000"):
        return True
    else:
        return False
    
# Check if the hash starts with six 0s
def check_if_correct_part_2(hash):
    if(hash[:6] == "000000"):
        return True
    else:
        return False    

data = 1
hashed = 0

# Increment until needed hash is found
while(True):
    hashed = hash(data, key)
    if(check_if_correct_part_1(hashed)):
        part_1_asnwer = data
        break
    data += 1

# Increment until needed hash is found
while(True):
    hashed = hash(data, key)
    if(check_if_correct_part_2(hashed)):
        part_2_asnwer = data
        break
    data += 1

print("Part 1: ", part_1_asnwer)
print("Part 2: ", part_2_asnwer)
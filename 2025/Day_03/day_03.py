f = open("input.txt", "r")
bateries = f.read()
f.close()

banks = bateries.splitlines()

count_of_banks = len(banks)

#Part 1

def find_max_joltage_in_bank_part_1(bank):
    max_joltage = 0

    for i, battery in enumerate(bank):
        if(i == len(bank) - 1):
            break
        for j, second_battery in enumerate(bank[i+1:]):
            if(int(battery + second_battery) > max_joltage):
                max_joltage =  int(battery + second_battery)

    return max_joltage

max_joltage_sum = 0

for bank in banks:
    max_joltage_sum += find_max_joltage_in_bank_part_1(bank)

# print("Sum of the max joltage in all banks (part 1) = ", max_joltage_sum)

# Part 2

def find_biggest_battery(bank):
    biggest_battery = 0
    for battery in bank:
        if(battery > biggest_battery):
                biggest_battery = battery
    
    return biggest_battery

def find_max_joltage_in_bank_part_2(bankstr):
    bank = []
    for battery in bankstr:
        bank.append(int(battery))

    # print(bank)

    max_joltage = 0

    biggest_battery_1 = find_biggest_battery(bank[:-11])
    # print("biggest_battery_1 = ", biggest_battery_1)
    for i_1, battery_1 in enumerate(bank[:-11]):
        if(battery_1 == biggest_battery_1):
            rest_of_bank_1 = bank[i_1+1:].copy()
            biggest_battery_2 = find_biggest_battery(rest_of_bank_1[:-10])
            # print("biggest_battery_2 = ", biggest_battery_2)
            # print("rest of bank 1 = ", rest_of_bank_1)
            for i_2, battery_2 in enumerate(rest_of_bank_1[:-10]):
                if(battery_2 == biggest_battery_2):
                    rest_of_bank_2 = rest_of_bank_1[i_2+1:].copy()
                    biggest_battery_3 = find_biggest_battery(rest_of_bank_2[:-9])
                    # print("biggest_battery_3 = ", biggest_battery_3)
                    # print("rest of bank 2 = ", rest_of_bank_2)
                    for i_3, battery_3 in enumerate(rest_of_bank_2[:-9]):
                        if(battery_3 == biggest_battery_3):
                            rest_of_bank_3 = rest_of_bank_2[i_3+1:].copy()
                            biggest_battery_4 = find_biggest_battery(rest_of_bank_3[:-8])
                            # print("biggest_battery_4 = ", biggest_battery_4)
                            # print("rest of bank 3 = ", rest_of_bank_3)
                            for i_4, battery_4 in enumerate(rest_of_bank_3[:-8]):
                                if(battery_4 == biggest_battery_4):
                                    rest_of_bank_4 = rest_of_bank_3[i_4+1:].copy()
                                    biggest_battery_5 = find_biggest_battery(rest_of_bank_4[:-7])
                                    # print("biggest_battery_5 = ", biggest_battery_5)
                                    # print("rest of bank 4 = ", rest_of_bank_4)
                                    for i_5, battery_5 in enumerate(rest_of_bank_4[:-7]):
                                        if(battery_5 == biggest_battery_5):
                                            rest_of_bank_5 = rest_of_bank_4[i_5+1:].copy()
                                            biggest_battery_6 = find_biggest_battery(rest_of_bank_5[:-6])
                                            # print("biggest_battery_6 = ", biggest_battery_6)
                                            # print("rest of bank 5 = ", rest_of_bank_5)
                                            for i_6, battery_6 in enumerate(rest_of_bank_5[:-6]):
                                                if(battery_6 == biggest_battery_6):
                                                    rest_of_bank_6 = rest_of_bank_5[i_6+1:].copy()
                                                    biggest_battery_7 = find_biggest_battery(rest_of_bank_6[:-5])
                                                    # print("biggest_battery_7 = ", biggest_battery_7)
                                                    # print("rest of bank 6 = ", rest_of_bank_6)
                                                    for i_7, battery_7 in enumerate(rest_of_bank_6[:-5]):
                                                        if(battery_7 == biggest_battery_7):
                                                            rest_of_bank_7 = rest_of_bank_6[i_7+1:].copy()
                                                            biggest_battery_8 = find_biggest_battery(rest_of_bank_7[:-4])
                                                            # print("biggest_battery_8 = ", biggest_battery_8)
                                                            # print("rest of bank 7 = ", rest_of_bank_7)
                                                            for i_8, battery_8 in enumerate(rest_of_bank_7[:-4]):
                                                                if(battery_8 == biggest_battery_8):
                                                                    rest_of_bank_8 = rest_of_bank_7[i_8+1:].copy()
                                                                    biggest_battery_9 = find_biggest_battery(rest_of_bank_8[:-3])
                                                                    # print("biggest_battery_9 = ", biggest_battery_9)
                                                                    # print("rest of bank 8 = ", rest_of_bank_8)
                                                                    for i_9, battery_9 in enumerate(rest_of_bank_8[:-3]):
                                                                        if(battery_9 == biggest_battery_9):
                                                                            rest_of_bank_9 = rest_of_bank_8[i_9+1:].copy()
                                                                            biggest_battery_10 = find_biggest_battery(rest_of_bank_9[:-2])
                                                                            # print("biggest_battery_10 = ", biggest_battery_10)
                                                                            # print("rest of bank 9 = ", rest_of_bank_9)
                                                                            for i_10, battery_10 in enumerate(rest_of_bank_9[:-2]):
                                                                                if(battery_10 == biggest_battery_10):
                                                                                    rest_of_bank_10 = rest_of_bank_9[i_10+1:].copy()
                                                                                    biggest_battery_11 = find_biggest_battery(rest_of_bank_10[:-1])
                                                                                    # print("biggest_battery_11 = ", biggest_battery_11)
                                                                                    # print("rest of bank 10 = ", rest_of_bank_10)
                                                                                    for i_11, battery_11 in enumerate(rest_of_bank_10[:-1]):
                                                                                        if(battery_11 == biggest_battery_11):
                                                                                            rest_of_bank_11 = rest_of_bank_10[i_11+1:].copy()
                                                                                            battery_12 = find_biggest_battery(rest_of_bank_11)
                                                                                            # print("biggest_battery_12 = ", battery_12)
                                                                                            # print("rest of bank 10 = ", rest_of_bank_10)
                                                                                            battery_sum = int(str(battery_1) + str(battery_2) + str(battery_3) + str(battery_4) + str(battery_5) + str(battery_6) + str(battery_7) + str(battery_8) + str(battery_9) + str(battery_10) + str(battery_11) + str(battery_12))          
                                                                                            if(battery_sum > max_joltage):
                                                                                                max_joltage =  battery_sum
    return max_joltage

max_joltage_sum = 0

for index, bank in enumerate(banks):
    max_joltage_sum += find_max_joltage_in_bank_part_2(bank)

print("Sum of the max joltage in all banks (part 2) = ", max_joltage_sum)
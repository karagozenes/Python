def names():
    with open ("Documents/22_names.txt","r") as file:
        content = file.read()
    list_ = content.replace("\"","").split(",")
    list_.sort()

    total = 0
    name_number = 0
    for name in list_:
        letter_sum = 0
        for letter in name:
            if letter == "A":
                letter_sum += 1
            elif letter == "B":
                letter_sum += 2
            elif letter == "C":
                letter_sum += 3
            elif letter == "D":
                letter_sum += 4
            elif letter == "E":
                letter_sum += 5
            elif letter == "F":
                letter_sum += 6
            elif letter == "G":
                letter_sum += 7
            elif letter == "H":
                letter_sum += 8
            elif letter == "I":
                letter_sum += 9
            elif letter == "J":
                letter_sum += 10
            elif letter == "K":
                letter_sum += 11
            elif letter == "L":
                letter_sum += 12
            elif letter == "M":
                letter_sum += 13
            elif letter == "N":
                letter_sum += 14
            elif letter == "O":
                letter_sum += 15
            elif letter == "P":
                letter_sum += 16
            elif letter == "Q":
                letter_sum += 17
            elif letter == "R":
                letter_sum +=18
            elif letter == "S":
                letter_sum += 19
            elif letter == "T":
                letter_sum += 20
            elif letter == "U":
                letter_sum += 21
            elif letter == "V":
                letter_sum += 22
            elif letter == "W":
                letter_sum += 23
            elif letter == "X":
                letter_sum += 24
            elif letter == "Y":
                letter_sum += 25
            elif letter == "Z":
                letter_sum += 26

        name_number += 1
        total += letter_sum *name_number
    return total

print(names())
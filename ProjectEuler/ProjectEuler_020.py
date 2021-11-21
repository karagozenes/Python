from math import factorial

def sum_factorial(x):

    str_num = str(factorial(x))
    total = 0
    for i in str_num:
            total += int(i)
    return total

print(sum_factorial(100))
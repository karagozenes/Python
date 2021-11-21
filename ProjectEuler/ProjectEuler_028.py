def spiral():
    (start,increment,total) = (1,2,1)
    for i in range(500):
        for j in range(4):
            start += increment
            total += start
        increment +=2

    return total

print(spiral())
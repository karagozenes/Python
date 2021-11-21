from math import sqrt

for x in range(1,1000):
    for y in range(1,1000):
        z = sqrt((x**2) + (y**2))
        if x+y+z == 1000:
            print(x,y,z,x*y*z)
            break
        else:
            continue

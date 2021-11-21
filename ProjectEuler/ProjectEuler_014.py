from time import time
st = time()

highestnum,highestchain = 0,0
cnum = 0
for cnum in range(2,100000):
    chain = 1
    num = cnum
    while True:
        if num == 1:
            if chain > highestchain:
                highestchain = chain
                highestnum = cnum
            break
        if num %2 == 0:
            num = num/2
            chain +=1
        else:
            num = 3*num+1
            chain += 1

print(highestnum,highestchain)

et = time()
print(et-st)
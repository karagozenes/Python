from math import *

def prime(num):
    prime = True
    for i in range(2,int(abs(num)**0.5)+1):
        if num%i == 0:
            prime = False
            break
    if prime == True and num !=0 and num != 1:
        return prime

def Quadratic():
    (max_primes,max_a,max_b) = (0,0,0)
    for a in range(-999,1000):
        for b in range(-1000,1001):
            (n,count) = (0,0)
            while True:
                value = n**2 + a*n + b
                if prime(value) == True and prime(value) == True:
                    count += 1
                    n += 1
                    if count > max_primes:
                        (max_primes,max_a,max_b) = (count,a,b)
                else:
                    break
    return (max_primes, max_a, max_b, max_a*max_b)

print(Quadratic())
def divisors(x):
    half_divs = [i for i in range(1,int(x**0.5)+1) if x%i == 0]
    other_divs = []
    for i in reversed(half_divs):
        if i == 1:
            continue
        other_divs.append(x//i)
    divisors = half_divs + other_divs
    return sum(divisors)

def amicable():
    amicable_list = []
    for num1 in range(1,10000):
        num2 = divisors(num1)
        if num1 == divisors(num2) and num1 != num2:
            amicable_list.append(num1)
    return sum(amicable_list)

print(amicable())
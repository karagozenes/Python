def one_four():
    first_list = set()
    for i in range(1,10):
        for j in range(1000,10000):
            result = i*j

            str_all =str(i) + str(j) + str(result)
            pandigital = set()
            for k in str_all:
                pandigital.add(k)
            if  len(str(i)) == 1 and len(str(j)) == 4 and len(str(result)) == 4 and len(pandigital) == 9 and "0" not in pandigital:
                first_list.add(result)
    return sum(first_list)

def two_three():
    second_list = set()
    for i in range(10,100):
        for j in range(100,1000):
            result = i*j

            str_all =str(i) + str(j) + str(result)
            pandigital = set()
            for k in str_all:
                pandigital.add(k)
            if  len(str(i)) == 2 and len(str(j)) == 3 and len(str(result)) == 4 and len(pandigital) == 9 and "0" not in pandigital:
                second_list.add(result)
    return (sum(second_list))

print(one_four() + two_three())

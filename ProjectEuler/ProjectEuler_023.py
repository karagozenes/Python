def proper_divs(x):
    proplist = set()
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            proplist.add(i)
            if i != 1:
                proplist.add(int(x/i))
    return proplist

def abundant_nums():
    abundant_list = []
    for i in range(12,28124):
        proper_divs(i)
        if sum(proper_divs(i)) >i:
            abundant_list.append(i)
    return abundant_list

def abundant_sum():
    list_ = abundant_nums()
    newlist = set()
    while True:
        if len(list_) != 0:
            for i in range(len(list_)):
                num = list_[0] + list_[i]
                if num <= 28123:
                    newlist.add(num)
                else:
                    break
            list_.pop(0)
        else:
            break
    return newlist

total = sum([x for x in range(1,28124)])

print(total - sum(abundant_sum()))
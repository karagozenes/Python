def func():
    list_ = []
    for i in range(2,1000000):
        value = str(i)
        product = 0
        for j in value:
            product += int(j)**5
        if product == int(value):
            list_.append(product)
    return list_

print(func())
print(sum(func()))
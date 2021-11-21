import itertools

nums = [0,1,2,3,4,5,6,7,8,9]
list_ = list(itertools.permutations(nums,10))
num = list_[999999]
result = ""
for i in num:
    result += str(i)

print(result)
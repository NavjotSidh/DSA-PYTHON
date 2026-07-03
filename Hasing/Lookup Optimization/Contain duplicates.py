def Contain_duplicate(num):
    return len(num) != len(set(num))
print(Contain_duplicate([1,2,3,4,5,5]))
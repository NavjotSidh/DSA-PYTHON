positive=0
negative=0
zero=0

arr = [3, -1, 0, 5, 3, -2, 5]
for i in arr:
    if i>0:
        positive=+1
    if i<0:
        negative= +1
    else:
        zero= +1
print(positive,negative,zero)
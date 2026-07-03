def Min_removal(x):
    count=0
    result=[]
    for i in x:
        if i=="(":
            result.append(i)
            count+=1
        elif i==")" and count > 0:
            result.append(i)
            count-=1
        elif i!=")":
            result.append(i)

    filtered=[]
    for i in result[::-1]:
        if i=="("and count>0:
            count-=1
        else :
            filtered.append(i)
    return "".join(filtered[::-1])
print(Min_removal("a)b(c)d("))

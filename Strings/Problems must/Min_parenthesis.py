def Min_parenthesis(arr):
    open_count=0
    invalid_count=0
    for i in arr:
        if i=="(":
            open_count+=1
        elif i==")":
            if open_count>0:
                open_count-=1
            else :
                invalid_count+=1
    return open_count+invalid_count
print(Min_parenthesis("))(()"))
def Min_add_parenthesis(s):
    open_count=0
    result=0
    for i in s:
        if i=="(":
            open_count+=1
        else:
            if open_count==0:
                result+=1
            open_count=max(open_count-1,0)
    return open_count+result
print(Min_add_parenthesis("()))(("))
child = [1, 2, 3, 4, 5]
cookie = [1, 1, 2, 3, 5]
def assign_cookie(child,cookie):
    child.sort()
    cookie.sort()
    i=0
    j=0
    while i <len(child) and j<len(cookie):
        if cookie[j]>=child[i]:
            i+=1
            j+=1
        else:
            j+=1
    return i
print(assign_cookie(child,cookie))
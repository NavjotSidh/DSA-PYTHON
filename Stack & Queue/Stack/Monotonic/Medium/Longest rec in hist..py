hist=[2,1,5,6,2,3]
def lon_rec(hist):
    n=len(hist)
    stack=[]
    maxarea=0

    for i,h in enumerate(hist):
        start=i
        while stack and stack[-1][1]>h:
            idx,hgt=stack.pop()
            maxarea=max(maxarea,hgt*(i-idx))
            start=idx
        stack.append((start,h))
    for i,h in stack:
        maxarea=max(maxarea,h*(n-i))
    return maxarea
print(lon_rec(hist))
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

l=max(weights)
r=sum(weights)

res=sum(weights)
while l<=r:
    mid=(l+r)//2

    curr=0
    day_needed=1
    for w in weights:
        if curr+w>mid:
            day_needed+=1
            curr=0
        curr+=w
    if day_needed<=days:
        res=min(res,mid)
        r=mid-1

    else:
        l=mid+1
print(res)
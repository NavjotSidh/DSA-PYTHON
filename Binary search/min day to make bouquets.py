bloomDay = [2, 10, 3, 10, 2]
m = 3
k = 1

l=1
r=max(bloomDay)

res=r
while l<=r:
    mid=(l+r)//2

    count=0
    bouquets=0
    for day in bloomDay:
        if day<=mid:
            count+=1
            if count==k:
                bouquets+=1
                count=0
        else:
            count=0

    if bouquets>=m:
        res=min(res,mid)
        r=mid-1
    else:
        l=mid+1
print(res)
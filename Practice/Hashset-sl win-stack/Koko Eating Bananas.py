import math

piles = [3, 6, 7, 11]
h = 8
l=1
r=max(piles)
while l<=r:
    mid=(l+r)//2
    hour=0
    for i in piles:
        hour+=math.ceil(i/mid)
    if hour<=h:
        r=mid-1
    elif hour>h:
        l=mid+1
print(l)
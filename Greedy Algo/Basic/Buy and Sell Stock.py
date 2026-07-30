prices = [1,2,3,4,5]
curr=1
prev=0
ans=0
while curr<len(prices):
    if prices[prev]>=prices[curr]:
        curr+=1
        prev+=1
    else:
        ans+=(prices[curr]-prices[prev])
        curr+=1
        prev+=1
print(ans)
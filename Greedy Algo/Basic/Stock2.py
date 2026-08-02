prices = [7,1,5,3,6,4]

min_price=prices[0]
ans=0

for i in prices:
    min_price=min(min_price,i)
    ans=max(ans,i-min_price)
print(ans)
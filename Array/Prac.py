prices = [7,1,5,3,6,4]
min_price=prices[0]
profit=0
for i in prices:
    min_price=min(min_price,i)
    profit=max(profit,i-min_price)
print(profit)
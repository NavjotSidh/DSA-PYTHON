jewels = "aA"
stones = "aAAbbbb"
jewels=set(jewels)
count=0
for i in stones:
    if i in jewels:
        count+=1
print(count)
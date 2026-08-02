s = "abccccdd"
freq={}
for i in s:
    freq[i] = freq.get(i, 0) + 1

length=0
odd =False

for count in freq.values():
    if count%2==0:
        length+=count
    else:
        length+=count-1
        odd=True
if odd:
    length+=1
print(length)
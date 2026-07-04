#Find the 2 most frequent elements
from unittest import result

arr = [1,3,3,2,2,3]
k = 2
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
result=sorted(freq ,key=freq.get, reverse=True)
print(result[:k])
nums = [1,1,1,2,2,3]
k = 2
freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1
a=sorted(freq, key=lambda x: freq[x],reverse=True)
print(a[:k])
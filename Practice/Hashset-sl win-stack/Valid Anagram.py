s = "anagram"
t = "nagaram"
freq={}
ans=True
if len(s)!=len(t):
    ans=False
for i in s:
    freq[i]=freq.get(i,0)+1

for j in t:
    if freq[j]<=0:
        ans=False
        break
    freq[j]-=1
print(ans)
from collections import defaultdict
s = "ABABAB"
k = 1
freq=defaultdict(int)
ans=0
maxFreq=0
l=0

for r in range(len(s)):
    freq[s[r]]+=1
    maxFreq=max(maxFreq,freq[s[r]])

    while (r-l +1)-maxFreq>k:
        freq[s[l]]-=1
        l+=1
    ans=max(ans,(r-l +1))
print(ans)

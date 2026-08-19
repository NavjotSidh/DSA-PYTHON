s="abccdcabacda"
N=len(s)
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
print(sorted(freq.items() ,key=lambda x:x[1])[0][1])

s = "AABABBA"
k = 1
freq={}
start=0
length=0
mx_freq=0
for i,num in enumerate(s):
    freq[num]=freq.get(num,0)+1
    mx_freq=max(mx_freq,freq[num])
    while (i-start+1)-mx_freq>k:
        freq[s[start]]-=1
        start+=1
    length=max(length,i+1-start)
print(length)
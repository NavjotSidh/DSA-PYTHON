s = "rat"
t = "car"
if len(s)!=len(t):
    ans=False
else:
    freq = {}
    ans = True

    for i,ch in enumerate(s):
        freq[ch]=freq.get(ch,0)+1
    for i in t:
        if i not in freq:
            ans=False
            break
        freq[i]-=1
        if freq[i]<0:
            ans=False
            break

print(ans)
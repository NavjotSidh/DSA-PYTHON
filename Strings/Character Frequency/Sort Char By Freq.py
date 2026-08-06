s = "tree"
def sort_by_freq(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    sfreq=sorted(freq.items(), key=lambda x: x[1], reverse=True)
    ans=""
    for ch,i in sfreq:
        ans+=ch*i
    return ans
print(sort_by_freq(s))
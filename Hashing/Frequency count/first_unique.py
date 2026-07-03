def First_unique(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    for i in s:
        if freq[i]==1:
            return i
    return None
print(First_unique("aabccd"))
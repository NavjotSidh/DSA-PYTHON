def Count_char_freq(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    return freq
print(Count_char_freq("banana"))

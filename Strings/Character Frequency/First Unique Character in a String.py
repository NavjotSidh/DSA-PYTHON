s = "loveleetcode"
def first_uniq_ch(s):
    freq={}
    for i,ch in enumerate(s):
        freq[ch]=freq.get(ch,0)+1
    for i,ch in enumerate(s):
        if freq[ch]==1:
            return i
print(first_uniq_ch(s))
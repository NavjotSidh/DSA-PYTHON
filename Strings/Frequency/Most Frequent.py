def Most_frequent(s):
    freq={}
    max_char=s[0]
    max_count=0
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    if freq[ch]>max_count:
        max_count=ch
        max_char=freq[ch]
    print(max_count,max_char)
Most_frequent('programmingg')
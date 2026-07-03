def Char_frequency(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    print("frequency of",s,'is',freq)
Char_frequency("banana")
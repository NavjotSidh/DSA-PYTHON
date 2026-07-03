def Check_Anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq={}
    for ch in s1.lower():
        freq[ch]=freq.get(ch,0)+1
    for ch in s2.lower():
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True
print(Check_Anagram("silent","Listen"))
def Count_word_freq(s):
    w=s.lower().split()
    freq={}
    for i in w:
        freq[i]=freq.get(i,0)+1
    return freq
print(Count_word_freq("Data science is fun and data is powerful"))
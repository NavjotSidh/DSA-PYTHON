def Word_frequency(S):
    words=S.split()
    freq={}
    for i in words:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print('Frequency of words in',S,'is',freq)
Word_frequency('this is a test this is simple')

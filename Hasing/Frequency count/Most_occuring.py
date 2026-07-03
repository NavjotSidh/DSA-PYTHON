def Most_occuring(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1

    return max(freq, key=freq.get)
print(Most_occuring([1, 2, 2, 3, 3, 3, 4,4,4,4,4]))
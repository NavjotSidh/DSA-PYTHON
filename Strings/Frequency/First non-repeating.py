def first_non_repeating(S):
    freq={}
    for ch in S:
        freq[ch]=freq.get(ch,0)+1

    for ch in S:
        if freq[ch]==1:
            print(ch)
            break
first_non_repeating('aabbccfdd')
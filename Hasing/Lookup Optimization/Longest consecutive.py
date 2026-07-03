def Longest_consecutive(s):
    num_set=set(s)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            current=num
            length=1

            while current+1 in num_set:
                length+=1
                current+=1
            longest=max(longest,length)
    return longest
print(Longest_consecutive([100, 4, 200, 1, 3, 2]))
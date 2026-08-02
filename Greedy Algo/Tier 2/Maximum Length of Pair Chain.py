pairs = [[1,2],[2,3],[3,4]]
pairs.sort()
count=1
prev_end=pairs[0][1]
for i in range(1,len(pairs)):
    if pairs[i][0]>prev_end:
        count+=1
        prev_end=pairs[i][1]
print(count)
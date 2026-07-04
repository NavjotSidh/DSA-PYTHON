# Insert a new interval into the list and merge if necessary.
intervals = [[1,3],[6,9]]
newInterval = [2,5]
for i in intervals:
    if newInterval[0]>=i[0] and newInterval[0]<=i[-1]:
        if i[0]>=newInterval[0]:
            i[0]=newInterval[0]
        elif i[-1]>=newInterval[0]:
            i[-1]=newInterval[-1]
        if i[-1]>newInterval[-1]:
            i[-1]=newInterval[-1]
    else:
        intervals.append(newInterval)
print(intervals)

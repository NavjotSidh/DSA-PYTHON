#Return the minimum number of intervals to remove so that the remaining intervals do not overlap.
def Non_overlap(intervals):
    intervals.sort(key=lambda x:x[0])
    prev_end=intervals[0][1]
    count=0
    for i in intervals:
        if prev_end<=i[0]:
            prev_end=i[1]
            continue
        elif prev_end>i[0]:
            count+=1
            prev_end=min(prev_end,i[1])
    return count
print(Non_overlap(intervals = [[1,100],[2,3],[4,5]]))
intervals = [[1,2],[2,3],[3,4],[1,3]]
def non_overlap(intervals):
    ans=0
    intervals.sort()
    prev_end=intervals[0][1]
    for i in range(1,len(intervals)):
        if prev_end<=intervals[i][0]:
            prev_end=intervals[i][1]
            continue
        else:
            ans+=1
            prev_end=min(prev_end,intervals[i][1])
    return ans
print(non_overlap(intervals))
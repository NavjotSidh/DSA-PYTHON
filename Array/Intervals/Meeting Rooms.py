#Determine if a person can attend all meetings.
def Meeting_room(intervals):
    intervals.sort(key=lambda x:x[0])
    prev_end=float('-inf')
    for i in intervals:
        if prev_end<=i[0]:
            prev_end=i[1]
        else :
            return False
    return True
print(Meeting_room(intervals = [[7,10],[2,4]]))
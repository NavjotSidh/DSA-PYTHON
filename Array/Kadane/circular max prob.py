def circular_maxima(arr):
    #min
    cur_sum=0
    mn=float('inf')
    for i in arr:
        cur_sum+=i
        mn=min(mn,cur_sum)
        if cur_sum>0:
            cur_sum=0
    total=sum(arr)
    #max
    mx = float('-inf')
    curr_sum=0
    for i in arr:
        curr_sum += i
        mx = max(mx, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    total = sum(arr)
    if mx<0:
        return mx
    if mn<0:
        c=total - mn
        return max(c,mx)

    return max(mx,total)
print(circular_maxima([8,-1, 3, 4]))
cost = [10, 15, 20]
def rec(i,cost):
    if i>=len(cost):
        return
    return cost[i]+min(rec(i+1,cost),rec(i+2,cost))
print(rec(0,cost))
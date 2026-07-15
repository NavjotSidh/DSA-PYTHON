
def rec(i,sm,arr,dp):
    total=sum(arr)
    if i>=len(arr):
        return False

    if sm>( total//2):
        return False

    if sm==(total//2):
        return True

    if dp[i][sm]!=-1:
        return dp[i][sm]
    #take
    take=rec(i+1,sm+arr[i],arr,dp)

    #not take
    not_take=rec(i+1,sm,arr,dp)

    dp[i][sm]= take or not_take
    return dp[i][sm]


def sub_sum(arr):
    total = sum(arr)
    n=len(arr)
    target=total//2
    dp = [[-1] * (target + 1) for _ in range(n)]
    if n==1:
        return False
    if total%2==1:
        return False
    return rec(0,0,arr,dp)

print(sub_sum([8,1,3,4,5,3]))
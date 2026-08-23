def balancedSums(arr):
    # Write your code here
    prefix=[0]*(len(arr)+1)
    prefix[0]=arr[0]
    ans="NO"
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    for i in range(len(prefix)-1):
        if i==0 and prefix[len(prefix)-2]==0:
            ans="YES"
            break
        elif prefix[i-1] == prefix[len(prefix)-2]-prefix[i]:
            ans= "YES"
            break
    return ans
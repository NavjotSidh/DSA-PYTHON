def birthday(s, d, m):
    # Write your code here
    total=sum(s[:m])
    ans=0
    if total==d:
        ans+=1
    for i in range(m,len(s)):
        total+=s[i]
        total-=s[i-m]
        if total==d:
            ans+=1
    return ans
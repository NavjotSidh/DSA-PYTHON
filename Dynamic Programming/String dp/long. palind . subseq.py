s = "bbbab"
def lps(i,j,s):
    if i==j:
        return 1
    if i > j:
        return 0
    if s[i]==s[j]:
        return 2+lps(i+1,j-1,s)
    l=lps(i+1,j,s)
    r=lps(i,j-1,s)
    return max(l,r)
print(lps(0,len(s)-1,s))
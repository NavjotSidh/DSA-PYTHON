#binary search with no consecutive 1's
def count(n,last=0):
    if n==0:
        return 1
    if last==1:
        return count(n-1,0)
    else:
        return count(n-1,0)+count(n-1,1)
print(count(3))
def solve(a):
    # Write your code here
    freq={}

    r=0
    for i in a:
      freq[i]=freq.get(i,0)+1

    for i in freq.values():

        if i>1:

            r+= i*(i-1)

    return r
print(solve([1,2,1,2,3,2,4,1]))
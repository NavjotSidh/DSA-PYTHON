def stock_span(arr):
    n=len(arr)
    ans=[1]*n
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if not stack:
            ans[i]=i+1
        else:
            ans[i]=i-stack[-1]
        stack.append(i)
    return ans
print(stock_span([100, 80, 60, 70, 60, 75, 85]))
price=[100,80,60,70,60,75,85]
def online_stock_span(prices):
    n=len(prices)
    stack=[]
    ans=[1]*n
    for i,price in enumerate(prices):
        while stack and price>=stack[-1][1]:
            idx=stack.pop()[0]
            ans[idx]=i-idx
        stack.append((i,price))
    return ans
print(online_stock_span(price))
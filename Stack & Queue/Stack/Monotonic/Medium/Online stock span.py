price=[100,80,60,70,60,75,85]
def online_stock_span(prices):
    n=len(prices)
    stack=[]
    ans=[1]*n
    for i,p in enumerate(prices):
        while stack and p>=stack[-1][1]:
            ans[i]+=ans[stack.pop()[0]]
        stack.append((i,p))
    return ans
print(online_stock_span(price))
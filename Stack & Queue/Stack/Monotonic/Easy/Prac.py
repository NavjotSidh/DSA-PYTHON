heights=[10,6,8,5,11,9]
def Visible(heights):
    n=len(heights)
    stack=[]
    ans=[0]*n

    for i in range(n-1,-1,-1):
        visible=0
        while stack and stack[-1]<heights[i]:
            visible += 1
            stack.pop()

        if stack:
            visible+=1
        ans[i]=visible
        stack.append(heights[i])
    return ans
print(Visible(heights))
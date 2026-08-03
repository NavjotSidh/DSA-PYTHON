temp = [73,74,75,71,69,72,76,73]
def dailytemp(temp):
    n=len(temp)
    stack=[]
    ans=[0]*n
    for i in range(n):
        while stack and temp[i] > temp[stack[-1]]:
            idx = stack.pop()
            ans[idx] = i - idx
        stack.append(i)
    return ans
print(dailytemp(temp))
def Dailt_temp(arr):
    res=[0]*len(arr)
    stack=[]
    for i,t in enumerate(arr):
        while stack and t>stack[-1][0]:
            stackvalue,stackind=stack.pop()
            res[stackind]=i-stackind
        stack.append((t,i))
    return res
print(Dailt_temp([73,74,75,71,69,72,76,73]))
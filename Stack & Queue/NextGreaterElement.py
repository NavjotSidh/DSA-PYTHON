# def NextGreaterElement(num1,num2):
#     #num1=[4,1,2]
#     #num2=[[1,3,4,2]
#     stack=[]
#     nge={}
#
#     for num in num2:
#         while stack and num>stack[-1]:
#             smaller=stack.pop()
#             nge[smaller]=num
#         stack.append(num)
#
#     for num in stack:
#         nge[num]=-1
#
#     return [nge[num] for num in num1]
# print(NextGreaterElement([4,1,2], [1,3,4,2]))

def Next_gretr(arr,arr2):
    n=len(arr)
    ans={}
    st=[]
    for i in range(n-1,-1,-1):
        while len(st)>0 and arr[i]>=st[-1]:
            st.pop()
        if len(st)==0:
            ans[arr[i]] = -1
        else:
            ans[arr[i]]=st[-1]
        st.append(arr[i])
    return list(map(lambda x:ans[x],arr2))
print(Next_gretr( [1,3,4,2],[4,1,2],))
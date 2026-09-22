# arr,target=[2, 7, 11, 15], 9
# seen={}
# ans=[]
# for i,num in enumerate(arr):
#     comp=target-num
#     if comp in seen:
#         ans=[i,seen[comp]]
#     seen[num]=i
# print(ans)
from TREES.Heap.Prac import freq

# arr=[7, 6, 4, 3, 1]
# mn=arr[0]
# profit=0
# for i in arr:
#     mn=min(mn,i)
#     profit=max(profit,i-mn)
# print(profit)

# arr=[-3, -1, -2]
# best=arr[0]
# curr=arr[0]
# for i in arr:
#     curr=max(curr+i,i)
#     best=max(best,curr)
# print(best)

# arr=[0, 1,3,4,0,0,0, 0, 3, 12]
# a=0
# f=0
# for f in range(len(arr)):
#     if arr[f]!=0:
#         arr[a],arr[f]=arr[f],arr[a]
#         a+=1
# print(arr)

# a,b="rat", "car"
# freq={}
# ans=True
# if len(a)!=len(b):
#     ans=False
# for i in a:
#     freq[i]=freq.get(i,0)+1
#
# for i in b:
#
#     if freq.get(i,0)<=0:
#         ans=False
#         break
#     freq[i]-=1
# print(ans)


# s="leetcode"
# seen={}
# for i in s:
#     seen[i]=seen.get(i,0)+1
# for i in range(len(s)):
#     if seen[s[i]]==1:
#         print(i)
#         break

# arr,k=[1, 2, 3, 4, 5, 6, 7], 3
# arr=arr[k+1:len(arr)]+arr[:k+1]
# print(arr)
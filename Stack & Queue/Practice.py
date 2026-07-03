#valid parenthesis
# def val_paren(s):
#     stack=[]
#     hash={")":"(","]":"[","}":"{"}
#     for ch in s:
#         if ch in hash.values():
#             stack.append(ch)
#         elif ch in hash:
#             if not stack or stack[-1] in hash:
#                 return False
#             stack.pop()
#     return len(stack)==0
# print(val_paren("({[]})"))
from inspect import stack


# Next greater element
# nums = [2,1,2,4,3]
# n=len(nums)
# stack=[]
# ans=[-1]*n
# for i in range(n):
#     while stack and nums[i]>nums[stack[-1]]:
#         e=stack.pop()
#         ans[e]=nums[i]
#     stack.append(i)
# print(ans)

#Next smaller element
# nums = [2,1,4,3]
# n=len(nums)
# stack=[]
# ans=[-1]*n
# for i in range(n):
#     while stack and nums[i]<nums[stack[-1]]:
#         e = stack.pop()
#         ans[e]=nums[i]
#     stack.append(i)
# print(ans)

#Daily Temperatures
# temp = [73,74,75,71,69,72,76,73]
# n=len(temp)
# ans=[0]*n
# stack=[] #(temp,index)
# for i ,t in enumerate(temp):
#     while stack and t>stack[-1][0]:
#        stacktemp,stackind= stack.pop()
#        ans[stackind]=i-stackind
#     stack.append([t,i])
# print(ans)

#Stock Span
# def stock_span(arr):
#     n=len(arr)
#     ans=[1]*n
#     stack=[]
#     for i in range(n):
#         while stack and arr[stack[-1]]<=arr[i]:
#             stack.pop()
#         if not stack:
#             ans[i]=i+1
#         else:
#             ans[i]=i-stack[-1]
#         stack.append(i)
#     return ans
# print(stock_span([100, 80, 60, 70, 60, 75, 85]))

#Min stack
# class Min_stack:
#     def __init__(self):
#         self.stack=[]
#         self.minstack=[]
#
#     def push(self,val:int):
#         self.stack.append(val)
#         if not self.minstack:
#             self.minstack.append(val)
#         else:
#             self.minstack.append(min(self.minstack[-1],val))
#
#     def pop(self):
#         self.stack.pop()
#         self.minstack.pop()
#
#     def min(self):
#         return self.minstack[-1]
#
#     def top(self):
#         return self.stack[-1]
# m1=Min_stack()
# m1.push(-2)
# m1.push(-3)
# m1.push(3)
# print(m1.min())
# print(m1.top())

# #6. Evaluate Reverse Polish Notation
# tokens = [2, 1, "+", 3, "*"]
# stack=[]
# for t in tokens:
#     if t in {"+","-","*","/"}:
#         a=stack.pop()
#         b=stack.pop()
#         if t=="+":
#             stack.append(a+b):
#         elif t=="-":
#             stack.append(a-b)
#         elif t=="*":
#             stack.append(a * b)
#         elif t=="/":
#             stack.append(a/b)
#     else:
#         stack.append(t)
# print(stack)

#largest Rectangle in Histogram
# nums=[2,1,5,6,2,3]
# n=len(nums)
# stack=[] #pair:(index,height)
# Maxarea=0
# for i,h in enumerate(nums):
#      start=i
#      while stack and stack[-1][1]>h:
#          index,height=stack.pop()
#          Maxarea=max(Maxarea,height*(i-index))
#          start=index
#      stack.append([start,h])
# for i,h in stack:
#     Maxarea=max(Maxarea,h*(n-i))
# print(Maxarea)

#
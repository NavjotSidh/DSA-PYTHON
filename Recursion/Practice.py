# #factorial
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
from unittest import result

# # Fibonacci
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(6))
# N=6
# for i in range(N):
#     print(fib(i))


# #Sum of N Numbers
# def sum(n):
#     if n<1:
#         return 0
#     return n+sum(n-1)
# print(sum(6))


# #Reverse an array
# def reverse(arr,left,right):
#     if left>=right:
#         return 0
#     arr[left],arr[right]=arr[right],arr[left]
#     reverse(arr,left+1,right-1)
# arr=[1,2,3,4,5,6]
# reverse(arr,0,len(arr)-1)
# print(arr)


# #Check Palindrome
# def paf(s,left,right):
#     if left>=right:
#         return True
#     if s.lower()[left]!=s.lower()[right]:
#         return False
#     return paf(s,left+1,right-1)
# s="Madam"
# print(paf(s,0,len(s)-1))


# #Print Subsequences
# nums=[5,9,7]
# result = []
# def solve(ind,subset):
#     if ind>=len(nums):
#         result.append(subset.copy())
#         return
#     subset.append(nums[ind])
#     solve(ind+1,subset)
#     subset.pop()
#     solve(ind+1,subset)
# solve(0,[])
# print(result)
#
# #Generate Subsequences with Sum K
# nums=[5,9,3,1,4]
# result = []
# target=9
# def solve(ind,sum,subset):
#     if sum==target:
#         result.append(subset.copy())
#         return
#     elif sum>target:
#         return
#     if ind>=len(nums):
#         return
#     subset.append(nums[ind])
#     sum+=nums[ind]
#     solve(ind+1,sum,subset)
#     e=subset.pop()
#     sum-=e
#     solve(ind+1,sum,subset)
# solve(0,0,[])
# print(result)

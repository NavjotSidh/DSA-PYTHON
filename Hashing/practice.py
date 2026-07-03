# #Q1. Count Frequency of Elements
# arr=[1,2,2,3,1,2]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(freq)

# #Q2. max frequency
# arr=[1,2,2,3,1,2]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
#     ans=max(freq,key=freq.get)
# print(ans)

# #Q3. Count Distinct Elements
# arr=[1,2,2,3,3,3]
# print(len(set(arr)))

# #Q4. First Non-Repeating Element
# arr=[4,5,1,2,0,4,5]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# for num in arr:
#     if freq[num]==1:
#         print(num)
#         break

# #Q4 Duplicates
# arr=[1,2,3,4]
# if len(arr)!=len(set(arr)):
#     print(True)
# else:
#     print(False)

# #Q5 longest substring without duplicate characters.
# s="abcbacdac"
# set1=set({})
# set1.add(s[0])
# left=0
# right=1
# ans=1
# n=len(s)
# while right<n:
#     while s[right] in set1:
#         set1.discard(s[left])
#         left+=1
#     set1.add(s[right])
#     right+=1
#     ans = max(ans, (right - left))
# print(ans)

# #Subarray sun  equals k
# arr=[1,2,3]
# k=3
# s=()
# for i in arr:
#     if i==k:
#
#Q10. Group Anagrams
words=["eat","tea","tan","ate","nat","bat"]
group={}
for w in words:
    key="".join(sorted(w))
    if key not in group:
        group[key]=[]
    group[key].append(w)
print(list(group.values()))
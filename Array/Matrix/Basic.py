matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j],end=" ")

#max elem
# maxi=matrix[0][0]
# for i in matrix:
#     for j in i:
#         maxi=max(j,maxi)
# print(maxi,end=" ")

#Min elem
# mini=matrix[0][0]
# for i in matrix:
#     for j in i:
#         mini=min(j,mini)
# print(mini,end=" ")

#sum
# sum=0
# for i in matrix:
#     for j in i:
#         sum+=j
# print(sum)

#Count even , odd numbers.
# even=odd=0
# for i in matrix:
#     for j in i:
#         if j%2==0:
#             even+=1
#         else:
#             odd+=1
# print("even",even,"odd",odd)

#Search for a number.
# target=5
# for i in matrix:
#     for j in i:
#         if j == target:
#             print("Element found at",j)
#             break
#

#Sum of each row.
# for i in matrix:
#     sum = 0
#     for j in i:
#         sum+=j
#     print(sum)

#Sum of each column.
row=len(matrix)
col=len(matrix[0])
for j in range(col):
    total=0
    for i in range(row):
        total+=matrix[i][j]
    print(total)
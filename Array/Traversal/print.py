arr=[1,2,7,85,6,8,-6,4]
# for i in arr :
#  print(i)

max_val=0
min_val=0

for i in arr:
    if i > max_val:
        max_val=i
    if i < min_val:
        min_val=i
print('Maximum value :',max_val)
print("Minimum value :",min_val)


arr = [2,2,1,1,1,1,2]
count={}
for i,nums in enumerate(arr):
    count[nums]=count.get(nums,0)+1
    if count[nums]>len(arr)/2:
        print(nums)
        break
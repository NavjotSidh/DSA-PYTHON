flowerbed = [1,0,0,0,0,0,1]
n = 2
for i in range(len(flowerbed)):
    if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
        n-=1
        flowerbed[i]=1
if n==0:
    print(True)
else:
    print(False)
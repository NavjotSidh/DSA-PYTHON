ratings = [1 ,3 ,4 ,5 ,2]
candies=[1]*len(ratings)
n=len(ratings)

#left to right
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        candies[i]=max(candies[i-1]+1,candies[i])

#right to left
for i in range(n-2,-1,-1):
    if ratings[i]>ratings[i+1]:
        candies[i]=max(candies[i],candies[i+1]+1)

print(sum(candies))
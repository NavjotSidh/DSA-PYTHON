people = [3,2,2,1]
limit = 3
def boats_save_people(people,limit):
    people.sort()
    boat=0
    n=len(people)
    l=0
    r=n-1
    while l<=r:
        if people[l]+people[r] <= limit :
            boat+=1
            l+=1
            r-=1
        else:
            boat+=1
            r-=1
    return boat
print(boats_save_people(people,limit))
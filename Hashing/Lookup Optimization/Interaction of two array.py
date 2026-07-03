def Interaction_of_two_array(a,b):
    result=set()
    set1=set(a)
    for i in b:
        if i in set1:
            result.add(i)
    return result
print(Interaction_of_two_array([2,6,8,4,0],[1,54,8,2,9,0]))
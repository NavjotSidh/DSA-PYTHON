Astroid=[5,10,-5]
def astroid_coll(astroid):
    stack=[]
    for i in astroid:
        alive = True

        while alive and i<0 and stack and stack[-1]>0:
            if stack[-1]<-i:
                stack.pop()

            elif stack[-1]== -i:
                stack.pop()
                alive=False
            else:
                alive=False

        if alive:
            stack.append(i)
    return stack
print(astroid_coll(Astroid))
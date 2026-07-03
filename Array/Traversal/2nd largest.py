largest = float('-inf')
second_largest = float('-inf')

arr = [3, -1, 0, 4, 3, -2, 5]
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
    elif i!=largest and i>second_largest:
        second_largest=i
print("Second largest:", second_largest)


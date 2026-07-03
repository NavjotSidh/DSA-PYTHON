
def max_product(arr):
    mx=mn=arr[0]
    for i in arr[1:]:
        old_mx=mx
        old_mn=mn
        mn = min(old_mn * i, i, old_mx * i)
        mx=max(old_mx*i,i,old_mn*i)

    return mx
print(max_product([-2,3,-4]))

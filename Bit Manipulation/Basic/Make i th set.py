N=9
print(bin(N))
#1101
i=2
set=N|1<<i
print(bin(set))
print("Make set: ",set)

#clear ith bit
clear= N&~(1<<i)
print(bin(clear))
print("Clear: ",clear)

#toggle ith bit
toogle=(N^(1<<i))
print(bin(toogle))
print("Toogle: ",toogle)

from collections import defaultdict

s=["eat", "tea", "tan", "ate", "nat", "bat"]
d=defaultdict(list)
for i in s:
    key="".join(sorted(i))
    d[key].append(i)
print(list(d.values()))
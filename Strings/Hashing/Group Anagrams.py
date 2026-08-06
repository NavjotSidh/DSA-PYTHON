from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def group_anagram(strs):
    groups=defaultdict(list)
    for word in strs:
        key="".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
print(group_anagram(strs))
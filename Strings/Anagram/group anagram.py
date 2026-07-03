from collections import defaultdict
def Group_anagram(words):
    group=defaultdict(list)
    for word in words:
        key="".join(sorted(word))
        group[key].append(word)

    return list(group.values())
print(Group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
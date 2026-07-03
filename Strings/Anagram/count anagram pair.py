from collections import defaultdict
def Count_anagram_pair(words):
    group=defaultdict(int)

    for word in words:
        key="".join(sorted(word))
        group[key]+=1

    count=0
    for freq in group.values():
        if freq >1:
            count+=freq*(freq-1)//2
    return count
print(Count_anagram_pair(["listen", "silent", "enlist", "rat", "tar"]))

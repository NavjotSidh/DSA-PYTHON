def freqQuery(queries):
    freq = {}
    count = {}
    ans = []
    for query in queries:
        if query[0] == 1:
            a = query[1]
            old_freq = freq.get(a, 0)
            new_freq = old_freq + 1
            freq[a] = new_freq
            if count.get(old_freq, 0) > 0:
                count[old_freq] -= 1
            count[new_freq] = count.get(new_freq, 0) + 1


        elif query[0] == 2:
            a = query[1]
            old_freq = freq.get(a, 0)
            if old_freq > 0:
                new_freq = old_freq - 1
                freq[a] = freq.get(a, 0) - 1
                if count.get(old_freq) > 0:
                    count[old_freq] -= 1
                if new_freq > 0:
                    count[new_freq] = count.get(new_freq, 0) + 1


        else:
            a = query[1]
            if count.get(a, 0) > 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans
print(freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]))
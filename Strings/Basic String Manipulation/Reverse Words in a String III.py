s = "Let's take LeetCode contest"
def Reverse_word(s):
    words=s.split()
    for i,word in enumerate(words):
        words[i]=words[i][::-1]
    return " ".join(words)
print(Reverse_word(s))
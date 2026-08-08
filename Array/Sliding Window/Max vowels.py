s = "abciiidef"
k = 3

vowels = "aeiou"

count = 0

# First window
for i in range(k):
    if s[i] in vowels:
        count += 1

max_vowels = count

# Slide window
for i in range(k, len(s)):

    # Add new character
    if s[i] in vowels:
        count += 1

    # Remove old character
    if s[i - k] in vowels:
        count -= 1

    max_vowels = max(max_vowels, count)

print(max_vowels)
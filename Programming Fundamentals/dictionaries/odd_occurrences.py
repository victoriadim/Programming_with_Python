words = input().split(" ")
odd_words = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in odd_words:
        odd_words[word_lower] = 0
    odd_words[word_lower] += 1

for key, value in odd_words.items():
    if value % 2 != 0:
        print(key, end=" ")
sentence =  input("Enter the sentence to test:").lower()
word_freq = {}
for word in sentence.split():
    if word[-1] in ".!":
        word = word[:-1]
    word_freq[word] = word_freq.get(word,0) + 1
print(word_freq)
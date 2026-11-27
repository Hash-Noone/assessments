def word_frequencies(text):
    frequencies = {}

    for word in text.lower().split():
        cleaned_word = word.strip(".,!?;:'\"()[]{}")
        if cleaned_word:
            if cleaned_word in frequencies:
                frequencies[cleaned_word] += 1
            else:
                frequencies[cleaned_word] = 1

    return frequencies



sample_text = input("Enter your sentence here: ")
max_word = ""
max_freq = 0
dic = word_frequencies(sample_text)
for key in dic:
    if dic[key] > max_freq:
        max_freq = dic[key]
        max_word = key

print(f"Most frequent word: {max_word} appearing {max_freq} times ")

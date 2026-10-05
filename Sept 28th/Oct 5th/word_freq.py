from functools import reduce

def count_words(words):
    frequencies = {}

    for word in words:
        cleaned_word = word.strip(".,!?;:'\"()[]{}")
        if cleaned_word:
            if cleaned_word in frequencies:
                frequencies[cleaned_word] += 1
            else:
                frequencies[cleaned_word] = 1

    return frequencies

def most_frequent(dic):
    values = list(dic.keys())
    print(values)
    return reduce(lambda a, b: a if values.count(dic[a]) >= values.count(dic[b]) else b, dic)

sample_text = input("Enter your sentence here: ").lower().split()
dic = count_words(sample_text)
max_word = most_frequent(dic)
print(f"Most frequent word: {max_word} appearing {dic[max_word]} times ")

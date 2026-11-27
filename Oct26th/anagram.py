def find_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    dict1 = {}
    dict2 = {}
    for char in word1:
        dict1[char] = dict1.get(char, 0)+1 
    for char in word2:
        dict2[char] = dict2.get(char, 0)+1 
    return dict1 == dict2

sentence = input("Enter your two word seperated by a comma: ").lower().split(",")
if len(sentence) == 2:
    if find_anagrams(sentence[0], sentence[1]):
        print("Anagram")
    else:
        print("Not an anagram")
else:
    print("Only two words")
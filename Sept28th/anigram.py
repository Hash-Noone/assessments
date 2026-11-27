def find_anagrams(word1, word2):
    groups = {}
    if len(word1) != len(word2):
        return False
    checker = list(word2)
    for char in word1:
        if char in checker:
            checker.remove(char)
        else:
            return False
    return True


word1 = "listen"
word2 = "silent" 
result = find_anagrams(word1.lower(), word2.lower())
if result:
    print("Anagram")
else:
    print("Not an anagram")

def word_break(s, word_dict):
    if not s:
        return True
    index = 0
    while index <= len(s):
        if s[:index] in word_dict:
            if word_break(s[index:], word_dict):
                return True
        index += 1
    return False

# s = "leetcode" 
# word_dict = ["leet", "code"]
# Output:  True

# s = "applepenapple"
# word_dict = ["apple", "pen"]
# Output:  True

s = "catsandog" 
word_dict = ["cats", "do", "an","sand", "and", "cat","dog"]
# Output:  False
print(word_break(s,word_dict))
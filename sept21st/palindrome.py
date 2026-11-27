def pali(word):
    for ind in range(len(word)//2):
        if word[ind].lower() != word[-ind-1].lower():
            return False
    return True

word = input("Word to check: ")

if pali(word):
    print("Palindrome")
else:
    print("Not a Palindrome")
def is_palindrome(word):
    cleaned_word = word.replace(" ", "")
    right = len(cleaned_word) - 1
    left = 0
    while left < right:
        if cleaned_word[left].lower() != cleaned_word[right].lower():
            return False
        left += 1
        right -= 1
    return True

word = input("Enter the word to check: ")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

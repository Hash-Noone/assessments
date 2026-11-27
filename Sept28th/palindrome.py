def palindrome(s):
    right = len(s) - 1
    left = 0
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

sentence = input("Enter a string to check if it's a palindrome: ").lower()
if palindrome(sentence):
    print("Palindrome.")
else:
    print("Not a palindrome.")
def is_palindrome(s, right, left):
    if right <= left:
        return True

    #Had an issue with writing the incrementing my pointers without without a while loop
    if not is_letter(s[left]):
        left += 1
    if not is_letter(s[right]):
        right -= 1
    if is_letter(s[right]) and is_letter(s[left]) and s[left] != s[right]:
        return False
    elif is_letter(s[right]) and is_letter(s[left]) and s[left] == s[right]:
        return is_palindrome(s, right - 1, left + 1)
    else:
        return is_palindrome(s, right, left)
    


def is_letter(ch):
    if ch.isalpha():
        return True
    return False


sentence = input("Enter a string to check if it's a palindrome: ").lower()
right = len(sentence) - 1
left = 0
if is_palindrome(sentence,right,left):
    print("Palindrome.")
else:
    print("Not a palindrome.")
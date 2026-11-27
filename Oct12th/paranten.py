def balance_barackets(word):
    stack = []
    for char in word:
        if char == "(":
            stack.append(char)
        if char == ")":
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


user_input = input("Enter the numbers seperated by commas: ").strip()
test = user_input if user_input else "((a+b) * (c-d))"

if balance_barackets(test):
    print("Balanced")
else:
    print("Not balanced")

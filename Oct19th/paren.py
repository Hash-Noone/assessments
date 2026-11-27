def balance_barackets(word):
    stack = []
    for char in word:
        if char in "({[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif char == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    return True


user_input = input("Enter the expression: ").strip()
test = user_input if user_input else "((a+b) * [c-d])"

if balance_barackets(test):
    print("Balanced")
else:
    print("Not balanced")

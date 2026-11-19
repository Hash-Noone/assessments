def evaluate(expr, i = None):
    if i is None:
        i = len(expr) -1
    if i == 0:
        return expr
    if expr[i] == "+":
        return int(evaluate(expr[:i])) + int(evaluate(expr[i+1:]))
    if expr[i] == "-":
        return int(evaluate(expr[:i])) - int(evaluate(expr[i+1:]))
    if expr[i] == "*":
        try:
            return int((expr[:i])) * int((expr[i+1:]))
        except ValueError:
            return evaluate(expr, i-1)
    return evaluate(expr, i-1)

print(evaluate("8+2*9-6*2-8"))

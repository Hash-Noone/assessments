res_stack = []
output = 0
while True:
    input_str = input("Enter a operator  (+, -, *, /) and number separated by a space or undo to undo or 'exit' to quit: ")
    if input_str.lower() == 'exit':
        break
    elif input_str.lower() == 'undo':
        if res_stack:
            output = res_stack.pop()
            print("Last operation undone., operation result is now:", output)
        else:
            print("No operations to undo.")
            continue
    else:
        try:
            op, num = input_str.split()
            num = float(num)
            if op not in ['+', '-', '*', '/']:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            if not res_stack and op in ['*', '/']:
                print("Cannot perform multiplication or division without a previous result.")
                continue
            else:
                if op == '+':
                    output += num
                elif op == '-':
                    output -= num
                elif op == '*':
                    output *= num
                elif op == '/':
                    if num == 0:
                        print("Cannot divide by zero.")
                        continue
                    output /= num
            res_stack.append(output)
            print(f"Current result: {output}")
        except ValueError:
            print("Invalid input. Please enter an operator followed by a number.")
            continue
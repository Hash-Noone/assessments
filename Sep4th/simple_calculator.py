def add(first, second):
    return first + second
def subtract(first, second):
    return first - second
def multiply(first, second):
    return first * second
def divide(first, second):
    return first / second


try:
    first_number = float(input("Enter your first number: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

operator = input("operator (+, -, *, /): ")
if operator not in ["+", "-", "*", "/"]:
    print("Please enter a valid operator.")
    exit()

try:
    second_number = float(input("Enter your second number: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

match operator:
    case "+":
        result = add(first_number, second_number)
    case "-":
        result = subtract(first_number, second_number)
    case "*":
        result = multiply(first_number, second_number)
    case "/":
        if second_number == 0:
            print("Cannot divide by zero.")
            exit()
        result = divide(first_number, second_number)

print(result)
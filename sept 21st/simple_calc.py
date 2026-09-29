def num():
    try:
        num = int(input("Enter the number:"))
    except ValueError:
        return "Enter a number"
    return num

first_number = num()
operator = input("Enter the operator /, *, +, - :")
second_number = num()

if isinstance(first_number,int) and isinstance(second_number, int):
    if operator in "/*+-":
        match operator:
            case "+":
                result = first_number + second_number
            case "-":
                result = first_number - second_number            
            case "/":
                if second_number == 0:
                    result = "Cannot divide by zero"
                else: 
                    result = int(first_number / second_number)
            case "*":
                result = first_number * second_number
    else:
        result = "Invalid operator"
else:
    result = "Invalid number"

print(result)
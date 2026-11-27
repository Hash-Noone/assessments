while True:
    try:
        number = int(input("Enter your valid number: "))
        break
    except ValueError:
        print("Enter a valid integer")
binary = ""
while number > 0:
    binary = str(number%2) + binary
    number //= 2
print(binary)
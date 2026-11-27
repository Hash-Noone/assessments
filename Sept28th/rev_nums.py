def reverse_number(num):
    if num == 0:
        return 0

    negative = num < 0
    num = abs(num)
    reversed_num = 0

    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10

    if negative:
        reversed_num *= -1

    return reversed_num

while True:
    try:
        number = int(input("Enter your valid number: "))
        break
    except ValueError:
        print("Enter a valid integer")
print(reverse_number(number))
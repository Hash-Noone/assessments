nums = input("Enter the numbers:")
numbers = []
for num in nums.split(","):
    numbers.append(int(num))

largest = -float("inf")
second_largest = -float("inf")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and num > second_largest:
        second_largest = num
print(second_largest)
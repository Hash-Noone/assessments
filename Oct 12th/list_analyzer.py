user_input = input("Enter the numbers seperated by commas: ").strip()
test = [int(num) for num in user_input.split(",")] if user_input else [12, 5, 27, 8, 14]

smallest = float("inf")
largest = -float("inf")
total = 0
count = 0
for num in test:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    total += num
    count += 1
print(f"""
Smallest : {smallest}
Largest : {largest}
Total : {total}
Average : {total/count}""")

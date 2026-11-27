user_input = input("Enter the numbers seperated by commas: ").strip()
test = [int(num) for num in user_input.split(",")] if user_input else [14, 7, 22, 9, 7, 31]
user_input2 = input("Enter the target: ").strip()
target = int(user_input2) if user_input2 else 7
count = 0
for num in test:
    if num == target:
        print(f"Found at index {count}")
        break
    count += 1
else:
    print("Target not found")
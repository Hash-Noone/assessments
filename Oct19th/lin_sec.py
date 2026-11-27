user_input = input("Enter the numbers seperated by commas: ").strip()
test = [int(num) for num in user_input.split(",")] if user_input else [7, 22, 9, 7, 31, 7, 5]
user_input2 = input("Enter the target: ").strip()
target = int(user_input2) if user_input2 else 7
count = []
for index, num in enumerate(test):
    if num == target:
        count.append(index)
if count:
    print(f"Target: {target} → Found at indices: {count} | Count: {len(count)} | First: {count[0]} | Last: {count[-1]}")
else:
    print("Target not found")
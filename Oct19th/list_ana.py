user_input = input("Enter the numbers seperated by commas: ").strip()
test = [int(num) for num in user_input.split(",")] if user_input else [12, 5, 27, 8, 14, 27, 3]

smallest = 0
largest = 0
total = 0
count = 0
for index in range(len(test)):
    if test[smallest] > test[index]:
        smallest = index
    if test[largest] < test[index]:
        largest = index
    total += test[index]
    count += 1
average = round(total/count, 2)
count = 0
for num in test:
    if num > average:
        count += 1

print(f"""
Smallest : {test[smallest]} (at index {smallest})
Largest : {test[largest]} (at index {largest})
Total : {total}
Average : {average}
Numbers above average: {count}""")

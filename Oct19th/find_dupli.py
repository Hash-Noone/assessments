user_input = input("Enter the chars seperated by commas: ").strip()
test = [int(num) for num in user_input.split(",")] if user_input else [14, 7, 22, 9, 7, 31, 7, 5]
dic = {}
for num in test:
    dic[num] = dic.get(num,0) + 1
for key in dic:
    if dic[key] > 1:
        print(f"{key} has {dic[key] -1} more duplicates")

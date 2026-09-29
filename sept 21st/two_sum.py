numbers =  [3, 8, 8, 7, 6,12]  
target =  15

# for i in range(len(numbers[1:])):
#     for j in range(len(numbers[1:])):
#         if numbers[i] + numbers[j+1] == target:
#             print(f"Index = {[i , j+1]} \nNumbers to get target = {[numbers[i], numbers[j+1]]}")
#             exit()
# print(" No sum found")
dic = {}
for index in range(len(numbers)):
    if target - numbers[index] in dic:
        print(f"Index = {[dic[target - numbers[index]] , index]}\
               \nNumbers to get target = {target - numbers[index], numbers[index]}"
               )
        exit()
    dic[numbers[index]] = index
print(" No sum found")
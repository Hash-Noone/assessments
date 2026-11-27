def fizzbuzz_plus(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError
    if n < 0:
        raise ValueError
    total = []
    dic = {3:"Fizz", 5:"Buzz", 7:"Bazz"}
    for i in range(1,n+1):
        result = [dic[num] for num, _ in dic.items() if i % num == 0]
        if not result:
            result.append(str(i))
        total.append("".join(result))
    return total

print(fizzbuzz_plus(105))


# def stats(nums):
#     smallest = float("inf")
#     largest = -float("inf")
#     total = 0
#     for num in nums:
#         if num > largest:
#             largest = num
#         if num < smallest:
#             smallest = num
#         total += num
#     average = round(total / len(nums), 2)
#     return smallest, largest, average

# print(stats([-1,-3,-2]))

# def count_letters(text):
#     vowels, consonants = 0, 0
#     for char in text.lower():
#         if "a" <= char <= "z" :
#             if char in {"a", "e", "i", "o", "u"}:
#                 vowels += 1
#             else:
#                 consonants += 1
#     return vowels, consonants

# print(count_letters("Hello, World 123"))


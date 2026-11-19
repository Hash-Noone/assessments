# def count_paths(rows, cols):
#     return 0 if rows < 1 or cols < 1 else 1 if rows == 1 or cols == 1 else count_paths(rows-1, cols) + count_paths(rows, cols-1)

# print(count_paths(7, 3))

# def reverse_stack(stack, i = 0, j = None):
#     if j is None:
#         j = len(stack) - 1
#     if i >= j:
#         return stack
#     stack[i] , stack[j] = stack[j] , stack[i]
#     return reverse_stack(stack, i + 1, j - 1)
# stack = [1, 2, 3, 4, 5]
# print(reverse_stack(stack))

# def can_sum(nums, target, i=0, total= 0):
#     if total == target:
#         return True
    
#     if i == len(nums):
#         return False

#     return can_sum(nums, target, i + 1, total + nums[i]) or can_sum(nums, target, i + 1, total)
# nums = [3, 5, 7]
# target = 12

# print(can_sum(nums, target))

# def is_match(text, pattern):
#     if not text and (not pattern or pattern == "*"):
#         return True
#     if not text or not pattern :
#         return False
#     if pattern[0] == text[0] or pattern[0] == "?":
#         return is_match(text[1:], pattern[1:])
#     if pattern[0] == "*":
#         return is_match(text[1:], pattern[1:]) or is_match(text, pattern[1:]) or is_match(text[1:], pattern)

# text = "abc" 
# pattern = "*"


# print(is_match(text, pattern))
    
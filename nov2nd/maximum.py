def brute(nums):
    max_sum = float("-inf")
    indices = []
    for index, _ in enumerate(nums):
        total = 0
        for indexs, num2 in enumerate(nums[index:], start= index):
            total += num2
            if total > max_sum:
                max_sum = total
                indices = [index, indexs]
    return max_sum, indices

def sin_pas(nums):
    max_sum = float("-inf")
    current_sum = sum(nums)
    left = 0
    right = len(nums)-1
    indices = []
    while left <= right:
        if current_sum > max_sum:
            max_sum = current_sum
            indices = [left, right]
        if nums[left] < nums[right]:
            current_sum -= nums[left]
            left += 1
        else:
            current_sum -= nums[right]
            right -= 1
    return max_sum, indices




nums = [-2, 1, -3,  4, -1, 2, 1, -5, 4]
print(sin_pas(nums))
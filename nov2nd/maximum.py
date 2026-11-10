def brute(nums):
    max_sum = float("-inf")
    indices = []
    for index, num1 in enumerate(nums):
        total = num1
        for indexs, num2 in enumerate(nums[index+1:], start= index+1):
            # print(indexs,index)
            total += num2
            if total > max_sum:
                max_sum = total
                indices = [index, indexs]
    for index, num in enumerate(nums):
        if num > max_sum:
            max_sum = num
            indices = [index, index]
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
            left += 1
            current_sum -= nums[left]
        else:
            right -= 1
            current_sum -= nums[right]
    return max_sum, indices




nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sin_pas(nums))
def rec_bin_sec(nums, target, left = None, right = None, count = None, index = -1):
    if left is None and right is None and count is None:
        left = 0
        right = len(nums)
        count = 0
    count += 1
    if not nums:
        return -1, count
    mid = (left + right) // 2
    if nums[mid] == target:
        index = mid
        return rec_bin_sec(nums, target, left, mid-1, count, index)
    if left > right:
        return index, count
    if nums[mid] < target:
        return rec_bin_sec(nums, target, mid+1, right, count, index)
    return rec_bin_sec(nums, target, left, mid-1, count, index)


nums = [1, 3, 3, 3, 5, 8] 
target = 3
print(rec_bin_sec(nums,target))


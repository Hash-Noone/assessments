def subset(nums, index = 0):
    if index >= len(nums):
        return [[]]
    first = nums[index]
    rest = nums[index + 1:]
    subsets_without_first = subset(rest, 0)
    subsets_with_first = [[first] + subset for subset in subsets_without_first]
    return subsets_without_first + subsets_with_first

def permute(nums, index = 0):
    if index >= len(nums):
        return [[]]
    first = nums[index]
    rest = nums[index + 1:]
    perms_without_first = permute(rest, 0)
    perms_with_first = []
    for perm in perms_without_first:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + [first] + perm[i:]
            perms_with_first.append(new_perm)
    return perms_with_first

print(subset([1,1,1]))
print(permute([1,2,1]))
def second_largest(numbers):
    
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    largest = second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        raise ValueError("There is no second largest distinct value.")

    return second


nums = [4, 9, 2, 9, 7]
print(second_largest(nums))

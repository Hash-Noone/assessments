def current_second_largest(num, second):
    if num > second:
            return True
    return False
def second_largest(numbers):
    
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    largest = second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and current_second_largest(num,second):
              second = num

    if second == float('-inf'):
        raise ValueError("There is no second largest distinct value.")

    return second


nums = [4, 9, 2, 9, 7]
print(second_largest(nums))

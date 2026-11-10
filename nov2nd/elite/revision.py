def is_balanced(string):
    dic = {
        "}":"{",
        "]":"[",
        ")":"("
    }
    stack = []
    max_depth = 0
    for char in string:
        if char in dic.values():
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char in dic.keys():
            if stack == [] or dic[char] != stack.pop():
                return False
    return not stack, max_depth

def insertionsort(arr):
    shift = 0
    comparisons = 0
    for i in range(1,len(arr)):
        temp = arr[i]
        while i > 0:
            comparisons += 1                
            if arr[i-1] > temp:
                shift += 1
                arr[i] = arr[i-1]
                i -= 1
            else:
                break
        arr[i] = temp
    return arr, comparisons, shift

def bubble_sort(arr):
    swaps = 0
    comparisons = 0
    for i in range(len(arr)):
        swapped = False
        if i > 0 and not swapped:
            break
        for j in range(len(arr)-1-i):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, comparisons, swaps

def selection_sort(arr):
    swaps = 0
    comparisons = 0
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            swaps += 1
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, comparisons, swaps

def merge_sort(arr):
    comparisons= writes = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half, left_comparisons, left_writes = merge_sort(left_half)
        right_half, right_comparisons, right_writes = merge_sort(right_half)

        comparisons += left_comparisons + right_comparisons
        writes += left_writes + right_writes

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            writes += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            writes += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            writes += 1

    return arr, comparisons, writes

def quick_sort(arr):

    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr

def digit_sum(num):
    return 0 if num == 0 else (num%10) + digit_sum(num//10)
def reverse_text(string):
    return "" if not string else string[-1] + reverse_text(string[:-1])
def count_char(text, tag):
    return (0 if not text 
            else 1 + count_char(text[1+len(tag):], tag) if text[0:len(tag)] == tag 
            else count_char(text[1:], tag)
            )

def power(num, exp):
    return (1/power(num, -exp) if exp < 0 
            else 0 if exp == 0 
            else num if exp == 1 
            else power(num, exp//2) * power(num, exp//2) if exp % 2 == 0 
            else num * power(num, exp - 1)
            )

def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result




der = ([[1, 2, 3,5],
        [4, 5, 6,6],
        [7, 8, 9,7],
        [10,11,12,8]]) 
print(spiral_order(der))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]


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

def restock(stock, item, qty):
    if qty < 1:
        return ("Can't restock with a quantity less than 1")
    stock[item] = stock.get(item,0) + qty
    return stock

def sell(stock, item, qty):
    if not stock.get(item,0):
        return ("Can't sell what we don't have")
    if not ( 1 < qty < stock.get(item)):
        return ("wrong quantity")
    stock[item] -= qty
    return stock, "ok"

def low_stock(stock, limit):
    return [key for key in stock if stock[key] < limit ]

def total_items(stock):
    return sum([value for value in stock.values()])

stock = {"rice": 10, "beans": 5}
print(total_items(stock) 
)


def valid(matrix):
    countx = 0
    counto = 0
    empty_count = 0

    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        return False

    for row in matrix:
        for play in row:
            if play not in ("X", "O", " "):
                return False

            if play == "X":
                countx += 1
            elif play == "O":
                counto += 1
            else:
                empty_count += 1

    is_valid = countx == counto or countx == counto + 1
    is_full = empty_count == 0

    return is_valid, is_full

def tictactoe(matrix):
    is_valid, is_full = valid(matrix)
    if not is_valid:
        return "Invalid"

    winners = set()

    for num in range(3):
        # Check rows
        if matrix[num][0] != " " and matrix[num][0] == matrix[num][1] == matrix[num][2]:
            winners.add(matrix[num][0])

        # Check columns
        if matrix[0][num] != " " and matrix[0][num] == matrix[1][num] == matrix[2][num]:
            winners.add(matrix[0][num])

    # Main diagonal
    if matrix[0][0] != " " and matrix[0][0] == matrix[1][1] == matrix[2][2]:
        winners.add(matrix[0][0])

    # Anti-diagonal
    if matrix[2][0] != " " and matrix[2][0] == matrix[1][1] == matrix[0][2]:
        winners.add(matrix[2][0])

    # Determine winner
    if len(winners) > 1:
        return "Invalid"

    if winners:
        return next(iter(winners)) + " wins"

    # Check draw
    if is_full :
        return "Draw"

    return "In progress"

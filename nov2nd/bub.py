def bubble_sort(arr, descending=False):
    swaps = 0
    comparisons = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            comparisons += 1
            condition = arr[j] < arr[j+1] if descending else arr[j] > arr[j+1]
            if condition:
                swaps += 1
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break
    return arr, comparisons, swaps


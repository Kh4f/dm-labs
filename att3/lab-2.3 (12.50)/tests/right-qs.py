# Quick Sort
# COMPLEXITY:
# Best case:  O(nlogn)
# Average:    O(nlogn)
# Worst case: O(n^2)

comparisons = 0

def partition(arr, left, right):
    global comparisons
    i = left  # индекс элемента, большего опорного
    j = right - 1  # индекс элемента, меньшего опорного
    pivot = arr[right]  # опорный элемент

    while i < j:
        while i < right and arr[i] < pivot:
            comparisons += 1
            i += 1
        comparisons += 1

        while j > left and arr[j] > pivot:
            comparisons += 1
            j -= 1
        comparisons += 1

        comparisons += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    comparisons += 1
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    # возврат медианы списка
    return i


def quick_sort(array, start, end):
    global comparisons
    comparisons += 1
    if start < end:
        partition_pos = partition(array, start, end)
        quick_sort(array, start, partition_pos - 1)
        quick_sort(array, partition_pos + 1, end)


s = "14 30 8 4 22 7 15 6 9 5 16 23 28 27 24 3"
arr = list(map(int, s.split()))
quick_sort(arr, 0, len(arr)-1)
print(arr)
print(comparisons)

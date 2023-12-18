# Quick Sort
# COMPLEXITY:
# Best case:  O(nlogn)
# Average:    O(nlogn)
# Worst case: O(n^2)

comparisons = 0


def quick_sort(array):
    length = len(array)
    global comparisons

    comparisons += 1
    if length <= 1:
        return array
    else:
        pivot = array[0]
        del array[0]

    items_greater = []
    items_lower = []

    for item in array:
        comparisons += 1
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


s = "14 30 8 4 22 7 15 6 9 5 16 23 28 27 24 3"
arr = list(map(int, s.split()))
print(arr)

sorted_arr = quick_sort(arr)
print(sorted_arr)

print(comparisons)

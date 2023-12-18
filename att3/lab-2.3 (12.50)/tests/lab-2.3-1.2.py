# Quick Sort
# COMPLEXITY:
# Best case:  O(nlogn)
# Average:    O(nlogn)
# Worst case: O(n^2)

from itertools import permutations

with open('../input.txt', 'r') as file:
    N = int(file.readline().strip())

# Генерация всех возможных перестановок списка размера N
all_permutations = [list(p) for p in permutations(list(range(1, N + 1)))]


comparisons = 0

def partition(arr, left, right):
    global comparisons
    pivot = arr[right]
    i = left
    j = right - 1

    while True:
        while i <= j and arr[i] <= pivot:
            comparisons += 1
            i += 1
        comparisons += 1

        while i <= j and arr[j] >= pivot:
            comparisons += 1
            j -= 1
        # компенсация (ласт сравнение было, но тело while не выполнялось)
        comparisons += 1

        comparisons += 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[right], arr[i] = arr[i], arr[right]

    return i


def quick_sort(array, start, end):
    global comparisons

    comparisons += 1
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)


lists_comps_dict = {}

for i, arr in enumerate(all_permutations):
    comparisons = 0
    quick_sort(arr.copy(), 0, len(arr) - 1)
    lists_comps_dict[i] = comparisons

max_comps = max(lists_comps_dict.values())

with open('../output.txt', 'w') as file:
    for k, v in lists_comps_dict.items():
        if v == max_comps:
            file.write(' '.join(map(str, all_permutations[k])) + '\n')

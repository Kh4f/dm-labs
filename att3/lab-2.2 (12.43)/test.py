import math


# Shell Sort
# COMPLEXITY:
# Best case:  O(nlogn)
# Average:    O(nlogn)
# Worst case: O(n^2)


def shell_sort(a):
    comparisons = 0
    n = len(a)
    gap = n // 2

    # Для каждого значения интервала
    while gap > 0:
        # выполняем сортировку вставками для этого интервала
        for i in range(gap, n):
            temp = a[i]
            j = i
            while True:
                comparisons += 1
                if j >= gap and a[j - gap] > temp:
                    a[j] = a[j - gap]  # сдвиг элемента на интервал вперед
                    j -= gap  # переходим к следующему элементу
                else:
                    break
            a[j] = temp  # вставляем элемент на его новое место
        gap //= 2

    return comparisons


s = "3 4 5 6 7 8 9 14 15 16 22 23 24 27 28 30"
arr = list(map(int, s.split()))
comparisons = shell_sort(arr)

print(comparisons)

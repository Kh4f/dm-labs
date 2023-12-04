import os

with open(os.path.abspath("input.txt"), 'r') as inputFile:
    arr = list(map(int, inputFile.readline().split()))


def binarySearch(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        comparisons += 1
        middle = (left + right) // 2

        if arr[middle] == target:
            break
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return comparisons


totalComparisons = 0
for i in range(1, len(arr) + 1):
    totalComparisons += binarySearch(arr, i)

averageComparisons = totalComparisons / len(arr)
with open(os.path.abspath("output.txt"), 'w') as outputFile:
    outputFile.write(f"{averageComparisons}")

print(averageComparisons)

# Вычислительная сложность O(log n), так как функция на каждоый итерации делит массив на 2, логарифмически уменьшая количество элементов поиска

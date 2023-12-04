import os

with open(os.path.abspath("input1.txt"), 'r') as inputFile:
    arr = list(map(int, inputFile.readline().split()))


def interpolation_search(target):
    comparisons = 0
    left, right = 0, len(arr) - 1

    while (left <= right) and (arr[left] <= target <= arr[right]):
        print(left <= right)
        comparisons += 1
        pos = left + ((right - left) // (arr[right] - arr[left]) * (target - arr[left]))

        if arr[pos] == target:
            break
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return comparisons


totalComparisons = 0
for i in range(1, len(arr) + 1):
    u = interpolation_search(i)
    print(u)
    totalComparisons += interpolation_search(i)

averageComparisons = totalComparisons / len(arr)
with open(os.path.abspath("output.txt"), 'w') as outputFile:
    outputFile.write(f"{averageComparisons}")

print(averageComparisons)

# В лучшем случае, когда элементы равномерно распределены, сложность будет O(log(log(n))). В худшем случае,
# особенно если элементы распределены неравномерно, сложность может упасть до O(n). Это происходит потому,
# что интерполяционный поиск выбирает позицию в зависимости от значения искомого элемента и распределения значений в
# массиве. В идеальных условиях это позволяет быстро приблизиться к искомому значению. Временная сложность: O(log2(
# log2 n)) для среднего случая и O(n) для наихудшего случая (когда элементы распределяются экспоненциально).
# Чтобы этот алгоритм работал правильно, сбор данных должен быть отсортирован и равномерно распределен!

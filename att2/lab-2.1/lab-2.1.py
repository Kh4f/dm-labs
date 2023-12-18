with open('input.txt', 'r') as inputFile:
    arr = list(map(int, inputFile.readline().split()))


def sequentialSearch(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            break

    return comparisons


# Вызов главной функции поиска для каждого элемента от 1 до N
totalComparisons = 0
for i in range(1, len(arr) + 1):
    totalComparisons += sequentialSearch(arr, i)

# Среднее количество сравнений
averageComparisons = totalComparisons / len(arr)
with open('output.txt', 'w') as outputFile:
    outputFile.write(f"{averageComparisons}")

print(averageComparisons)

# в лучшем случае, если искомый элемент находится в самом начале, то сложность O(1)
# В худшем случае функция проверит все n элементов, если искомы элемент находится в конце - линейная сложность O(n)

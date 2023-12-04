import os
with open(os.path.abspath("input.txt"), 'r') as inputFile:
    arr = list(map(int, inputFile.readline().split()))


def insertionSort(arr):
    comparisons = 0

    # Проходим по элементам массива со второгоо элемента
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1

        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr, comparisons


sortedArray, comparisonsNumber = insertionSort(arr)

with open(os.path.abspath("output.txt"), 'w') as outputFile:
    outputFile.write(f"{sortedArray}\n{comparisonsNumber}")

print(f"{sortedArray}\n{comparisonsNumber}")

# Вычислительная сложность insertionSort в худшем случае составляет О(n^2) (На самом деле N*(N-1)/2). Это потому что
# для каждого элемента (кроме первого) алгоритм выполняет сравнение с каждым из предшествующих элементов в худшем
# случае (когда массив отсортирован в обратном порядке).

# В лучшем случае, когда массив уже отсортирован, сложность будет O(n), потому что тогда для каждого элемента
# требуется только одно сравнение, чтобы убедиться, что элемент уже находится на правильном месте и не требует
# перемещения.

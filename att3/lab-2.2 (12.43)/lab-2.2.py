import math

# Shell Sort
# COMPLEXITY:
# Best case:  O(nlogn)
# Average:    O(nlogn)
# Worst case: O(n^2)


def shell_sort(a, hs):
    comparisons = 0
    n = len(a)

    # Для каждого значения интервала
    for gap in hs:
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

    return a, comparisons


def generate_hs1(n):
    hs = [1]
    s = 0
    while s < math.floor(math.log2(n)):
        hs.append(2 * hs[-1] + 1)
        s += 1
    return hs[:-1][::-1]


def generate_hs2(n):
    hs = [1]
    s = 0
    while s < (math.floor(math.log(2 * n + 1, 3)) - 1):
        hs.append(3 * hs[-1] + 1)
        s += 1
    return hs[:-1][::-1]


with open('input.txt', 'r') as file:
    arr = list(map(int, file.readline().split()))

n = len(arr)
hs1 = generate_hs1(n)
hs2 = generate_hs2(n)

arr1, comparisons1 = shell_sort(arr.copy(), hs1)
arr2, comparisons2 = shell_sort(arr.copy(), hs2)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, arr1)) + '\n')
    file.write(str(comparisons1) + ' ' + str(comparisons2) + '\n')

# Shaker Sort

# COMPLEXITY:
# Best case:  O(n)
# Average:    O(n^2)
# Worst case: O(n^2)

def shaker_sort(a):
    comparisons = 0
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        start = start + 1

    return comparisons


with open("input.txt", "r") as input_file:
    arr = list(map(int, input_file.readline().split()))

comparisons_count = shaker_sort(arr)

with open("output.txt", "w") as output_file:
    output_file.write(' '.join(map(str, arr)) + '\n')
    output_file.write(str(comparisons_count))

# print(str(arr)[1:-1].replace(", ", " "))
# print(comparisons_count)

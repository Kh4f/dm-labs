def Partition(list, left, right):
    v = list[left]
    i = left
    j = right + 1

    while True:
        j -= 1
        while list[j] > v:
            j -= 1
        i += 1
        while list[i] < v:
            i += 1
        if i < j:
            list[i], list[j] = list[j], list[i]
        else:
            break
    list[left], list[j] = list[j], list[left]
    return j

N = 4

def QuickSort(list, left, right):
    list[N+1] = float('inf')  # размещение барьера
    if left < right:
        v = Partition(list, left, right)
        QuickSort(list, left, v-1)
        QuickSort(list, v+1, right)

s = "14 30 8 4 22 7 15 6 9 5 16 23 28 27 24 3"
arr = list(map(int, s.split()))
print(arr)

QuickSort(arr, 0, len(arr)-1)
print(arr)

# print(comparisons)
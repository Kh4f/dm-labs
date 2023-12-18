import math
w = 5

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# def partition(arr, left, right):
#     i = left  # индекс элемента, большего опорного
#     j = right - 1  # индекс элемента, меньшего опорного
#     pivot = arr[right]  # опорный элемент
#
#     while i < j:
#         while i < right and arr[i] < pivot:
#             i += 1
#
#         while j > left and arr[j] > pivot:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]
#
#     # возврат медианы списка
#     return i

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high -= 1
        # компенсация (ласт сравнение было, но тело while не выполнялось)

        while low <= high and array[low] <= pivot:
            low += 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def select_opt(list, k, left, right):
    while True:
        d = right - left + 1
        if d <= w:
            insertion_sort(list, left, right)
            return left+k-1

        dd = d // w
        for i in range(1, dd+1):
            insertion_sort(list, left+(i-1)*w, left+i*w-1)
            list[left+i-1], list[left+(i-1)*w+math.ceil(w/2)-1] = list[left+(i-1)*w+math.ceil(w/2)-1], list[left+i-1]

        v = select_opt(list, math.ceil(dd/2), left, left+dd-1)
        list[left], list[v] = list[v], list[left]
        v = partition(list, left, right)
        temp = v-left+1

        if k == temp:
            return v
        elif k < temp:
            right = v - 1
        else:
            k -= temp
            left = v + 1


arr = [20, 12, 18, 16, 24, 10, 22, 14]

print(select_opt(arr, 4, 0, len(arr)-1))



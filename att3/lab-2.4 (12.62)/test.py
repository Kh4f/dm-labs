def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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

def findOrderStatistic(array, k):
    left, right = 0, len(array)-1
    k -= 1
    while True:
        mid = partition(array, left, right)

        if mid == k:
            return array[mid]
        elif k < mid:
            right = mid
        else:
            left = mid + 1

arr = [20, 12, 18, 16, 24, 10, 22, 14]
arr2 = arr.copy()
insertion_sort(arr2, 0, len(arr) - 1)
print(arr2)
print(findOrderStatistic(arr, 1))
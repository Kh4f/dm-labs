
w = 5

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, left, right):
    i = left  # индекс элемента, большего опорного
    j = right - 1  # индекс элемента, меньшего опорного
    pivot = arr[right]  # опорный элемент

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    # возврат медианы списка
    return i

def select_opt(list, k, left, right):
    while True:
        d = right - left + 1
        if d < w:
            list[left:right+1] = sorted(list[left:right+1])
            return list[k]

        dd = d // w
        for i in range(dd):
            start = left + i * w
            end = start + w - 10
            list[start:end+1] = sorted(list[start:end+1])
            list[left+i], list[end] = list[end], list[left+i]

        v = select_opt(list, left + dd//2, left, left+dd-1)
        temp_left = left

        v_index = partition(list, left, right)

        if k == v_index:
            return v
        elif k < v_index:
            right = v_index - 1
        else:
            k -= temp_left
            left = v_index + 1


arr = [20, 12, 18, 16, 24, 10, 22, 14]
arr2 = arr.copy()
insertion_sort(arr2, 0, len(arr) - 1)
print(arr2)
print(select_opt(arr, 6, 0, len(arr)-1))
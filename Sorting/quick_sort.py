def quick_sort(arr, start, end):
    if start >= end:
        return
    # 원소가 1인 경우 종료

    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while (left <= right and arr[left] <= arr[pivot]):
            left += 1

        while (left <= right and arr[right] >= arr[pivot]):
            right -= 1

        if left > right:  # 엇갈렸다면
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:  # 엇갈리지 않았다면
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [5, 6, 7, 8, 1, 2, 9]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
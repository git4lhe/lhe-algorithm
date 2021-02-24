def quick_sort(arr, start, end):
    if start >= end:
        return
    # 원소가 1인 경우 종료

    pivot = start
    left = start + 1
    right = end

    while (left <= right):

        # 피봇보다 더 큰값들을 찾아냄
        # 피봇 작으면 pass
        while (left <= right and arr[left] <= arr[pivot]):
            left += 1

        # 피봇보다 더 작은값들을 찾아냄
        # 피봇보다 크면 pass
        while (left <= right and arr[right] >= arr[pivot]):
            right -= 1

        # left가 right보다 인덱스가 더 크다는것은
        # 피봇보다 더 큰 값들이 많았다는 거임
        if left > right:  # 엇갈렸다면
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:  # 엇갈리지 않았다면
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [5, 6, 15, 8, 9, 12, 9]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
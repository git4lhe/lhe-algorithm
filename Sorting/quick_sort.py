def quick_sort(arr, start, end):
    if start >= end:
        return
    # 원소가 1인 경우 종료

    pivot = start
    left = start + 1
    right = end
    p_value = arr[pivot]

   #피봇 작은거-> <-큰것것
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
        if left > right:  # 엇갈렸다면 left가 피봇보다 작은것 찾아냄
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:  # 엇갈리지 않았다면
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)
import random
import time
arr = [random.randint(1,1000) for x in range(1000)]
now = time.time()
quick_sort(arr, 0, len(arr) - 1)
print(time.time() - now)

def pythonic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x>= pivot]

    return pythonic_quick_sort(left_side) + [pivot] + pythonic_quick_sort(right_side)

arr = [random.randint(1,1000) for x in range(1000)]
now = time.time()
pythonic_quick_sort(arr)
print(time.time() - now)
print("finish")
def solution(arr):
    if len(arr) == 0:
        return -1

    minimum = min(arr)
    arr.remove(minimum)

    if not arr:
        return [-1]

    else:
        return arr
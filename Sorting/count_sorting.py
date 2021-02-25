import random

def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for v in arr:
        count[v] += 1

    sorted = []
    for i in range(1,len(count)):
        for j in range(count[i]):
            sorted.append(i)

    return sorted

arr = [random.randint(1,10) for _ in range(10)]
print(arr)
print(counting_sort(arr))

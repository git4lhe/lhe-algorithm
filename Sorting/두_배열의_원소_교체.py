def solution(arr_a,arr_b,k):
    arr_a.sort()
    arr_b.sort(reverse=True)

    for i in range(k):
        # 최대 k번이기 때문에
        # 반드시 a,b 원소비교를 하고, 바꾸어줌
        if a[i] < b[i]:
            a[i], b[i] = b[i] ,a[i]
        else:
            break
    return sum(arr_a)

a = [1,2,5,4,3]
b = [5,5,6,6,5]
print(solution(a,b,3))







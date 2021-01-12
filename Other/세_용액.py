# https://www.acmicpc.net/problem/2473
import sys # 강제로 끝낼 때, 필요
n = int(input())
arr = sorted(list(map(int,input().split())))

result = [None,None,None]
sum_value = float("inf") # inifinity number

# 3가지 수를 더했을 때, 0에 제일 가까운 값 찾기!
for i in range(len(arr)-2):
    left,right = i+1, len(arr)-1
    # arr[i] == arr[i-1] -> 전 루프값과 지금 루프값이 같으면!!! 바로 스킵가능

    if i > 0 and arr[i] == arr[i-1]:
        continue

    # 3-SUM method
    while(left < right):
        tmp = arr[i]+arr[left]+arr[right]

        # 0에 더 가까운 결과값 저장
        if abs(tmp) < abs(sum_value):
            sum_value = tmp
            result = [arr[i],arr[left],arr[right]]

        # 다른 경우 찾기
        if tmp < 0: # 0보다 작을 경우, left 값 +1
            left += 1
        elif tmp > 0:
            right -= 1 # 0보다 클 경우, right 값 -1
        else:
            # 찾으면 바로 끝내기
            print(arr[i],arr[left],arr[right])
            sys.exit(0)

print(result[0],result[1],result[2])





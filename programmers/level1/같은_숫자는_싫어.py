def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.


    # for문 i,j를 적절히 못바꿀꺼같음
    # 포인터 개념으로 풀기
    i,j = 0,1
    while 1:
        if j >= len(arr):
            break

        if arr[i] == arr[j]:
            j += 1

        else:
            answer.append(arr[i])
            i = j
            j = i+1

    # 마지막 i,j 반영해줌
    answer.append(arr[i])

    return answer
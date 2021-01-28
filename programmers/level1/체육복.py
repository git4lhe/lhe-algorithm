## HARD ##

def solution(n, lost, reserve):
    count = 0
    # 여벌 체육복을 가져온 학생이 체육복을 도난 당했을 수 있음
    # meaning : lost/reserve에서 같은 값을 갖을 수 있음

    j = 0
    n_lost = sorted(list(set(lost) - set(reserve)))
    n_reserve = sorted(list(set(reserve) - set(lost)))

    for i in range(len(n_lost)):

        while j < len(n_reserve):
            if n_reserve[j] > n_lost[i] + 1:
                break

            if n_reserve[j] == n_lost[i] - 1:
                count += 1
                j += 1
                break
            if n_reserve[j] == n_lost[i] + 1:
                count += 1
                j += 1
                break

            j += 1

    return n - len(n_lost) + count
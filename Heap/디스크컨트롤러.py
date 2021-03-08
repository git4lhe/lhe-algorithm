import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    count, last = 0, -1  # 작업 끝낼때까지의 검사에 필요한 변수, 작업 시작시간(-1은 작업이 없는 경우로 초기화시킴)
    time = jobs[0][0]  # 현재 상태/시간
    length = len(jobs)
    wait = []

    while count < length:
        # last 와 time안에 job이 들어온다면 wait 힙에 넣음
        for s, t in jobs:  # start, term 소요된 시간
            if last < s <= time:
                # job의 들어온 시간이 마지막 시간과 time 사이에 있어야 함
                heapq.heappush(wait, (t, s))
                # 첫번째 요소로 heap에서 알아서 정렬됨

        # 만약 wait안에 요소가 있다면 꺼냄
        if len(wait) > 0:
            last = time  # 3ms -> 6ms 작업 으로 바꿀때,
            term, start = heapq.heappop(wait)
            count += 1
            time += term  # ex) 6ms 경우 time = (3ms + 6ms)
            answer += (time - start)

        else:
            time += 1

    return answer // length


print(solution([[0, 3], [1, 9], [2, 6]]))
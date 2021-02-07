import heapq
# 이상.이하, 부등호,equal 매우 중요
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville:
        sco = heapq.heappop(scoville)
        if sco >= K:
            break
        else:
            if scoville:
                sco += heapq.heappop(scoville) * 2
                heapq.heappush(scoville,sco)
                answer += 1
            else:
                return -1

    return answer

print(solution([1,2,2],50))

l = [1,2,3,1,2,4,5]
h = heapq
h.heapify(l)
print(l)
print(h.heappop(l))
print(h.heappop(l))
print(h.heappop(l))
print(h.heappop(l))
print(h.heappop(l))
h.heappush(l, 1)
print(l) # [1, 4, 5]
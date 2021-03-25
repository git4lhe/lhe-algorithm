def solution(routes):

    answer = 0
    routes = sorted(routes, key= lambda x: x[0])

    cctv = [0] * len(routes)
    for i in range(0, len(routes)):
        if not cctv[i]:
            answer += 1
            cctv[i] = True
            exit = routes[i][1]
            for j in range(i+1,len(routes)):
                if routes[j][0] <= exit:
                    cctv[j] = True
                    if routes[j][1] >= exit:
                        continue
                    else:
                        exit = routes[j][1]
                else:
                    break
    return answer

print(solution([[-20,15], [-14,10], [-18,-13], [-5,-3]]))
print(solution([[-20,15], [-14,10], [-13,10], [-5,-3]]))



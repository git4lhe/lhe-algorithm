def solution(prices):
    answer = [1] * len(prices)
    leng = len(prices)

    for i in range(leng):
        for j in range(i+1, leng):
            if prices[i] > prices[j]:
                break
        print(i,j)
        answer[i] = j-i

    return answer

print("answer",solution([1, 2, 3, 2, 3]))


#[4, 3, 1, 1, 0]
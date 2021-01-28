def solution(answers):
    correct = [0, 0, 0]
    supos = [[1, 2, 3, 4, 5],
             [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for n, supo in enumerate(supos):
        for i in range(len(answers)):
            if answers[i] == supo[i % len(supo)]:
                correct[n] += 1

    answer = []
    find = max(correct)
    for i in range(3):
        if find == correct[i]:
            answer.append(i + 1)

    return answer
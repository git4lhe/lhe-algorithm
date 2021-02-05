def solution(dartResult):
    dartResult = [i for i in dartResult]

    score = [0, 0, 0]
    for i in range(3):
        num = dartResult.pop(0)
        if num.isdigit():
            if dartResult[0].isdigit():
                dartResult.pop(0)
                num = 10

            score[i] += int(num)

            while dartResult:
                if dartResult[0] in 'SDT*#':
                    chr = dartResult.pop(0)
                    if chr == 'D':
                        score[i] = pow(score[i], 2)
                    elif chr == 'T':
                        score[i] = pow(score[i], 3)
                    elif chr == 'S':
                        pass
                    elif chr == '*':
                        if i != 0:
                            score[i - 1] = score[i - 1] * 2
                            score[i] = score[i] * 2
                        else:
                            score[i] = score[i] * 2
                    else:
                        score[i] = score[i] * -1
                    continue
                else:
                    break

    return sum(score)
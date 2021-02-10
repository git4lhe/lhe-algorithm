def solution(s):
    answer = []

    count = 0
    zero_num = 0

    while (1):
        count += 1
        one_num = s.count("1")
        zero_num += len(s) - one_num

        s = format(one_num, 'b')
        if s == "1":
            return [count, zero_num]

    return answer
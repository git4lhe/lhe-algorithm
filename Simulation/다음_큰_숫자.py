def solution(n):
    bin_num = format(n,"b")
    num_one = bin_num.count("1")

    answer = n
    while (1):
        answer += 1
        tmp_bin = format(answer, "b")
        tmp_num_one = tmp_bin.count("1")

        if num_one == tmp_num_one:
            break
    return answer

print(solution(15))
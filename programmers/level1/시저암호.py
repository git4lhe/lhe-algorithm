def solution(s, n):
    answer = ""

    string = "abcdefghijklmnopqrstuvwxyz"
    string_up = string.upper()

    for ss in s:
        if ss.isalpha():
            if ss.islower():
                answer += string[(string.index(ss) + n) % len(string)]

            elif ss.isupper():
                answer += string_up[(string_up.index(ss) + n) % len(string)]
        else:
            answer += ss

    return answer
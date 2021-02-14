def solution(s):
    s = s.lower()
    answer = s[0].upper()
    for idx in range(1, len(s)):
        if s[idx-1].isspace() and s[idx].isalpha():
            answer += s[idx].upper()
            continue
        answer += s[idx]

    return answer
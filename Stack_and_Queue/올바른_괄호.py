def solution(s):
    stack = []

    for chr in s:
        if chr == "(":
            stack.append(chr)

        else:
            if stack:
                p = stack[-1]
                if p == "(":
                    stack.pop()
                    continue
            else:
                return False

    if stack:
        return False

    return True

print(solution("(()("))
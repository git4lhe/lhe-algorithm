from collections import deque


def solution(s):
    stack = []
    s = deque(s)

    while s:
        if stack:
            v = s.popleft()
            if stack[-1] == v:
                stack.pop()
            else:
                stack.append(v)

        else:
            stack.append(s.popleft())

    if stack:
        return 0

    return 1
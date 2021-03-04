def compare(word, target):
    cnt = 0
    for w, t in zip(word, target):
        if w != t:
            cnt += 1
    if cnt == 1:
        return True
    return False

from collections import deque
def solution(begin, target, words):
    if not target in words:
        return 0

    visited = [False] * len(words)
    stacks = deque()
    stacks.append((begin,0))

    # breath-first-search, answer는 거리를 말함
    while stacks:
        current,dis = stacks.popleft()
        if current == target:
            return dis

        for i in range(len(words)):
            if compare(words[i],current):
                if not visited[i]:
                    visited[i]=True
                    stacks.append((words[i],dis+1))
    return 0
print(solution("hit", "hhh", ["hhh","hht"]))
from collections import Counter

def solution(s):
    cnt = Counter(s.lower())

    if cnt['p'] == cnt['y']:
        return True

    return False
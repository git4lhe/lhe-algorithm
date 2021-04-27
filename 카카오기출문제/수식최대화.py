from itertools import permutations
from collections import deque
import copy
def solution(expression):

    answer = []
    opers = ['+','-','*']

    # 높을수록 우선순위 높음
    tolist = deque([])
    n = ""
    for ex in expression:
        if ex in opers:
            tolist.append(n)
            tolist.append(ex)
            n = ""
        else:
            n += ex
    tolist.append(n)

    for ops in permutations(opers,3):
        tmp_tolist = copy.deepcopy(tolist)

        for op in ops:
            tmp = deque([])
            while tmp_tolist:
                t = tmp_tolist.popleft()
                if t == op:
                    v1 = tmp.pop()
                    v2 = tmp_tolist.popleft()
                    tmp.append(str(eval(v1+op+v2)))
                else:
                    tmp.append(t)
            tmp_tolist = tmp

        if len(tmp_tolist) == 1:
            answer.append(abs(int(tmp_tolist.pop())))
    print(answer)
    return max(answer)

solution("100-200*300-500+20")
solution("50*6-3*2")
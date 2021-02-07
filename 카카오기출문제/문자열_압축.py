def solution(s):
    answer = 1e6

    for i in range(1, len(s)// 2 + 1):

        ret = ""
        count = 1
        prev = s[:i]

        for j in range(i,len(s)+i,i):
            if prev == s[i:j]:
                count += 1
            else:
                if count != 1:
                    ret += str(count) + prev
                else:
                    ret += prev

                count = 1
                prev = s[j:j+i]
                print("prev", j, j+i, prev)
        answer = min(len(ret), answer)

    return answer

string = "aabbaccc"
print(string[7:10])
print(solution("aabbaccc"))
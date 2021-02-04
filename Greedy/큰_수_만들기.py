def dsolution(number, k):
    answer = []

    for i in range(len(number)):
        while answer and answer[-1] < number[i] and k > 0:
            answer.pop()
            k -= 1

        if k == 0:
            answer += number[i:]
            break
        answer.append(number[i])

    if k>0:
        answer = answer[:-k]
    answer = "".join(answer)
    return answer

def solution(number, k):
    stack = []
    for index, num in enumerate(number):
        while stack and  stack[-1] < num and k >0:
            stack.pop()
            k-=1

        if k ==0:
            stack += number[index:]
            break
        stack.append(num)
    if k > 0:
        stack = stack[:-k]
    answer = "".join(stack)
    return answer

def ddsolution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    print(stack)
    return ''.join(stack)

print(solution("8223", 1))








def solution(numbers):

    numbers = list(map(str,numbers))
    answer = sorted(numbers, key=lambda x: x*3,reverse=True)
    return str(int("".join(answer)))


print(solution( [0,0,0,0]))
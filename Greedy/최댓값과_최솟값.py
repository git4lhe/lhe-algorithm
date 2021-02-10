def solution(s):
    answer = ''

    numbers = [int(i) for i in s.split(' ')]
    answer = "{} {}".format(min(numbers), max(numbers))

    return answer
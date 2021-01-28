def sum_val(number):
    if number < 10:
        return number
    return (number % 10) + sum_val(number // 10)

def solution(x):
    if x == 0:
        return False

    value = sum_val(x)
    print(x, value)
    if x % value == 0:
        return True

    return False

print(solution(12))
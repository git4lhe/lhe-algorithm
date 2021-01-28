def step12(x):
    x = x.lower()
    a = ""
    for i in x:
        if i.isalpha() or i.isdigit() or i == '-' or i == '.' or i == '_':
            a += i
    return a


def step34(x):
    a = ""
    for i in range(len(x)):
        if x[i] == x[i - 1] and x[i] == '.':
            continue
        a += x[i]

    if len(a) and a[0] == '.':
        a = a[1:]
    if len(a) and a[-1] == '.':
        a = a[:-1]

    return a


def step56(x):
    if len(x) == 0:
        x = 'a'
    elif len(x) >= 16:
        x = x[:15]

        if x[-1] == '.':
            x = x[:-1]

    return x


def step7(x):
    if len(x) <= 2:
        nx = x[-1] * (3 - len(x))
        x = x + nx

    return x


def solution(new_id):
    a = step12(new_id)
    a = step34(a)
    a = step56(a)

    return step7(a)
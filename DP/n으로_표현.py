
def multiply(value ,number):
    if value == 0:
        return
    return int(eval(str(value ) +str(number)))

def solution(N, number):
    tree = [N]

    nn = [N]
    for i in range(1,5):
        nn.append(int(eval(str(nn[i-1]) + str(N))))

    for i in range(8):
        sub_tree = []
        for t in tree:
            sub_tree.append(t + N)
            sub_tree.append(t * N)
            sub_tree.append(t - N)
            sub_tree.append(t // N)
            if t != 0:
                for i in range(4):
                    sub_tree.append(t + nn[i])

        if number in sub_tree:
            return i+1
        else:
            tree = list(sorted(set(sub_tree)))
    return -1

print(solution(5,12))



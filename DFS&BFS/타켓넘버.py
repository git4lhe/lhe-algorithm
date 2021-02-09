from itertools import permutations

def solution(numbers, target):
    tree=[0]

    for num in numbers:
        sub_tree = []
        for num2 in tree:
            sub_tree.append(num2 + num)
            sub_tree.append(num2 - num)
        tree = sub_tree

    return tree.count(target)


print(solution([1, 1, 1, 1, 1],3))
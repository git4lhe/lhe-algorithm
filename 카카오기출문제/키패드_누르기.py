def solution(numbers, hand):
    answer = ''

    keypad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        "*": (3, 0),
        0: (3, 1),
        "#": (3, 2)}

    left_list = [1, 4, 7]
    right_list = [3, 6, 9]

    curr = [(3, 0), (3, 2)]
    for n in numbers:
        if n in left_list:
            answer += 'L'
            curr[0] = keypad[n]
        elif n in right_list:
            answer += 'R'
            curr[1] = keypad[n]
        else:
            target = keypad[n]
            left_dis = abs(target[0] - curr[0][0]) + abs(target[1] - curr[0][1])
            right_dis = abs(target[0] - curr[1][0]) + abs(target[1] - curr[1][1])

            if left_dis > right_dis:
                answer += 'R'
                curr[1] = target
            elif left_dis < right_dis:
                answer += 'L'
                curr[0] = target

            elif left_dis == right_dis:
                # 거리가 같다면, 오른쪽잡이-오른쪽, 왼쪽잡이-왼쪽
                if hand == 'right':
                    curr[1] = target
                    answer += 'R'
                else:
                    curr[0] = target
                    answer += 'L'
    return answer
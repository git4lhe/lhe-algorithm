from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 트럭 1초 1
    # 다리길이, 무게 weight까지 견딤
    # 트럭이 다리에 완전히 오르지 않은 경우, 트럭의 무게는 고려x

    time = 0
    bridge = [0] * bridge_length

    # length, weight, truck_weight
    while len(bridge) != 0:
        time += 1
        # 1초 지남
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time

print(solution(2,10,[7, 4, 5, 6]))
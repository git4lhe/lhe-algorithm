def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    count = -1
    for i in range(a-1):
        count += days[i]
    count += b

    residue = count % 7

    return week[residue]
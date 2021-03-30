def get_min(num, b,c):

    if b > num:
        return 1

    if (num - b) % c > 0:
        result = (num-b) // c + 2
    else:
        result = (num - b) // c + 1

    return result

result = 0
people = dict()
N = int(input())
test_rooms = list(map(int,input().split()))
B,C = list(map(int,input().split()))

for num_people in test_rooms:
    if not num_people in people:
        people[num_people] = get_min(num_people,B,C )

for num_people in test_rooms:
    result += people[num_people]

print(result)

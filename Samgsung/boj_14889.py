from itertools import combinations
import sys

N = int(input())
minimum = sys.maxsize
skills = []
for i in range(N):
    row = list(map(int, input().split()))
    skills.append(row)

teams = [i for i in range(N)]

for team in combinations(teams, N // 2):
    other_team = list(set(teams) - set(team))

    team_a, team_b = 0,0
    for i in team:
        for j in team:
            team_a += skills[i][j]

    for i in other_team:
        for j in other_team:
            team_b += skills[i][j]

    minimum = min(minimum, abs(team_b-team_a))

print(minimum)

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        check = 0
        skill_check = 0

        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                skill_check += 1

            if skill_trees[i][j] == skill[check]:
                check += 1

            if check == len(skill):
                break
        if skill_check == check:
            answer += 1

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
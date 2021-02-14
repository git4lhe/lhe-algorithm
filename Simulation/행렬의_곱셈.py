def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    print(answer)
    for i, mat1 in enumerate(arr1):
        for j, mat2 in enumerate(zip(*arr2)):
            answer[i][j] = sum([n1 * n2 for n1, n2 in zip(mat1, mat2)])

    return answer


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
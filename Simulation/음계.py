input_data = list(map(int, input().split()))

answer = ''

for i in range(1, len(input_data) - 1):
    if input_data[i - 1] < input_data[i] < input_data[i + 1]:
        answer = 'ascending'

    elif input_data[i - 1] > input_data[i] > input_data[i + 1]:
        answer = 'descending'

    else:
        answer = 'mixed'
        break

print(answer)
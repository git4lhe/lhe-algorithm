# https://hiruby.tistory.com/298
N = int(input())
food = list(map(int, input().split()))

'''
4
1 3 1 5
'''
d = [0] * N
d[0] = food[0]
d[1] = max(food[0],food[1])

for i in range(2,N):
    d[i] = max(d[i-1],d[i-2]+food[i])

print(d[N-1])

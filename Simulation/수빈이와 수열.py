N = int(input())
B = list(map(int,input().split()))

A = [B[0]]
for n, i in enumerate(range(1,len(B))):
    value = B[i] * (i+1) - sum(A)
    A.append(value)

for i in A:
    print(i, end=" ")
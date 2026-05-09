N = int(input())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

X, Y = map(int, input().split())

print(A[X - 1][Y])
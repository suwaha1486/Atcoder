N, M = map(int, input().split())

grapes = M // N
person = M % N

for i in range(N):
    if i < person:
        print(grapes + 1)
    else:
        print(grapes)
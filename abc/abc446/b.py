N, M = map(int, input().split())

drink_set = set(range(1, M+1))

for i in range(N):
    L = int(input())
    X = list(map(int, input().split()))
    found = False
    for x in X:
        if x in drink_set:
            print(x)
            drink_set.remove(x)
            found = True
            break
    if not found:
        print(0)
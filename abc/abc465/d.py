T = int(input())

# if x > y:
# x < y * K < x + 1

for _ in range(T):
    X, Y, K = map(int, input().split())
    ans = 0
    while X != Y:
        if X < Y:
            X, Y = Y, X
        X = X // K
        ans += 1
    print(ans)
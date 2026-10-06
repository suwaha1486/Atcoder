N, D = map(int, input().split())
X = list(map(int, input().split()))

ans = []
for i in range(N):
    flg = True
    for j in range(N):
        if i == j:
            continue
        if abs(X[i] - X[j]) < D:
            flg = False
            break
        
    if flg:
        ans.append(i + 1)

print(len(ans))
if len(ans) > 0:
    print(*ans)
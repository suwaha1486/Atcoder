N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

ans = set()

# A1またはB1が必ず含まれる
for x in AB[0]:
    tmp = set(range(1, N+1))

    # xがいない組み合わせからyの候補を探す
    for a, b in AB:
        if x not in (a, b):
            tmp &= set([a, b])
        
    for y in tmp:
        if x != y:
            ans.add((min(x, y), max(x, y)))

print(len(ans))

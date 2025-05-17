from itertools import combinations

n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for comb in combinations(a, 5):
    if comb[0] % p * comb[1] % p * comb[2] % p * comb[3] % p * comb[4] % p == q:
        ans += 1

print(ans)

from collections import defaultdict

N = int(input())
D = defaultdict(int)

for i in range(N):
    S = input()
    s = S.lower()
    D[s] += 1

print(max(D.values()))
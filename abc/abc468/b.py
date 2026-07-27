M, D = map(int, input().split())
S = input()

check = [True] * M

for i in range(M):
    if S[i] == 'G':
        for j in range(max(0, i - D), min(M, i + D + 1)):
            check[j] = False

print(check.count(True))
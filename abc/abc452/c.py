from collections import defaultdict

N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

M = int(input())
S = []

for i in range(M):
    s = input()
    S.append(s)

# 文字 -> (位置, 文字列長)
alphabet = defaultdict(set)
for i in range(M):
    for j in range(len(S[i])):
        alphabet[S[i][j]].add((j + 1, len(S[i])))

for i in range(M):
    if len(S[i]) != N:
        print("No")
        continue

    for j in range(N):
        # alphabet[S[i][j]] で (B[j], A[j])が存在するか判定
        if (B[j], A[j]) in alphabet[S[i][j]]:
            continue
        else:
            print("No")
            break
    else:
        print("Yes")
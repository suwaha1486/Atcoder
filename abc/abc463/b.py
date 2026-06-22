N, X = input().split()
N = int(N)
alphabet_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
X_num = alphabet_num[X]

for i in range(N):
    S = input()
    if S[X_num] == 'o':
        print('Yes')
        exit()

print('No')
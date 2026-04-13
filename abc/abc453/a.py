N = int(input())
S = input()

for i in range(N):
    if S[i] != 'o':
        print(S[i:])
        exit()
    
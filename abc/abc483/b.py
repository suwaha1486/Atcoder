N, Q = map(int, input().split())
K = list(map(int, input().split()))

card = [i for i in range(1, N + 1)]

for k in K:
    card[:k] = [-x for x in card[:k][::-1]]
    
for i in range(N):
    print(card[i])
    
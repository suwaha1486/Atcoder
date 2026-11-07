from collections import defaultdict

N, M = map(int, input().split())

# kが辞退 -> A_i が B_iに移動

first = [[0, i] for i in range(N)] 
second = [defaultdict(int) for _ in range(N)]

for i in range(M):
    A, B  = map(int, input().split())
    first[A - 1][0] += 1
    second[A - 1][B - 1] += 1


ranking = sorted(first, key=lambda x: (-x[0], x[1]))

for i in range(N):
    if ranking[0][1] != i:
        max_votes = ranking[0][0]
        winner_idx = ranking[0][1]
    else:
        max_votes = ranking[1][0]
        winner_idx = ranking[1][1]
    
    for cand, cnt in second[i].items():
        if max_votes < first[cand][0] + cnt:
            max_votes = first[cand][0] + cnt
            winner_idx = cand
        elif max_votes == first[cand][0] + cnt and winner_idx > cand:
            winner_idx = cand

    print(winner_idx + 1)

S = [input() for _ in range(5)]

row_cnt = [0] * 5
col_cnt = [0] * 5
cross_cnt = [0] * 2

for i in range(5):
    for j in range(5):
        if S[i][j] == 'o':
            row_cnt[i] += 1
            col_cnt[j] += 1
            if i == j:
                cross_cnt[0] += 1
            if i + j == 4:
                cross_cnt[1] += 1

max_cnt = max(max(row_cnt), max(col_cnt), max(cross_cnt))
print(5 - max_cnt)
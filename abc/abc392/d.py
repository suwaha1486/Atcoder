from collections import Counter, defaultdict

n = int(input())

k = []
x_dict = defaultdict(list)
for i in range(n):
    tmp = list(map(int, input().split()))
    k.append(tmp[0])
    a_cnt = Counter(tmp[1:])
    for key, count in a_cnt.items():
        x_dict[key].append([i, count])
    
pair_sums = defaultdict(int)
for x, idx_cnt in x_dict.items():
    if len(idx_cnt) > 1:
        for idx1 in range(len(idx_cnt)):
            for idx2 in range(idx1+1, len(idx_cnt)):
                x_idx1, cnt1 = idx_cnt[idx1]
                x_idx2, cnt2 = idx_cnt[idx2]
                i, j = min(x_idx1, x_idx2), max(x_idx1, x_idx2)
                pair_sums[(i,j)] += cnt1 * cnt2

max_p = 0.0
for (i,j), comb_sum in pair_sums.items():
    p = comb_sum /(k[i] * k[j])
    max_p = max(max_p, p)

print(max_p)
h, w = map(int, input().split())

s = [[] for _ in range(h)]
for i in range(h):
    s[i] = list(input())

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            continue
        black_cnt = 0
        if i > 0:
            if s[i-1][j] == '#':
                black_cnt += 1
        if i < h - 1:
            if s[i+1][j] == '#':
                black_cnt += 1
        if j > 0:
            if s[i][j-1] == '#':
                black_cnt += 1
        if j < w - 1:
            if s[i][j+1] == '#':
                black_cnt += 1
        if black_cnt != 2 and black_cnt != 4:
            print('No')
            exit()

print('Yes')
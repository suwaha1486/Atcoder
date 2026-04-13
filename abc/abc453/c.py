N = int(input())
L = list(map(int, input().split()))

max_cnt = 0

for i in range(1 << N):
    pos = 0.5
    pre_pos = 0.5
    cnt = 0
    for j in range(N):
        if i >> j & 1:
            pos += L[j]
            if pre_pos < 0 and pos > 0:
                cnt += 1
            pre_pos = pos
        else:
            pos -= L[j]
            if pre_pos > 0 and pos < 0:
                cnt += 1
            pre_pos = pos

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
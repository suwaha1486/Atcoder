t = int(input())

for _ in range(t):
    flg = True
    n, h = map(int, input().split())
    pre_t = 0

    pre_h_upper = h
    pre_h_lower = h

    for i in range(n):
        t, l, u = map(int, input().split())

        h_upper = min(u, pre_h_upper + (t - pre_t))
        h_lower = max(l, pre_h_lower - (t - pre_t))

        if u < h_lower or l > h_upper:
            flg = False

        pre_h_upper = h_upper
        pre_h_lower = h_lower
        pre_t = t

    if flg:
        print('Yes')
    else:
        print('No')
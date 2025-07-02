t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    last = 0
    ans = 1
    ok = False
    used = [False] * n

    while True:
        if a[last] * 2 >= a[-1]:
            ans += 1
            ok = True
            break

        nxt = -1
        for i in range(1, n):
            if used[i]:
                continue
            if a[last] * 2 >= a[i]:
                if nxt == -1 or a[i] > a[nxt]:
                    nxt = i

        if nxt == -1 or a[nxt] <= a[last]:
            break

        last = nxt
        ans += 1
        used[nxt] = True

    if ok:
        print(ans)
    else:
        print(-1)

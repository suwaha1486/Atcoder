n, q = map(int, input().split())

nest_cnt = [1] * (n + 1)
pigeon = [i for i in range(n + 1)]

two_nest = set()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, h = query[1], query[2]
        nest_cnt[pigeon[p]] -= 1
        if pigeon[p] in two_nest and nest_cnt[pigeon[p]] < 2:
            two_nest.discard(pigeon[p])
        pigeon[p] = h
        nest_cnt[h] += 1
        if nest_cnt[h] > 1:
            two_nest.add(h)
    elif query[0] == 2:
        print(len(two_nest))
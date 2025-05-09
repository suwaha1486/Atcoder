n, q = map(int, input().split())
pigeon_idx = [i for i in range(n + 1)]
idx_nest = [i for i in range(n + 1)]
nest_idx = [i for i in range(n + 1)]

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        pigeon_idx[a] = nest_idx[b]

    elif query[0] == 2:
        a, b = query[1], query[2]
        
        tmp_idx_nest = idx_nest[nest_idx[a]]
        idx_nest[nest_idx[a]] = idx_nest[nest_idx[b]]
        idx_nest[nest_idx[b]] = tmp_idx_nest

        tmp_nest_idx = nest_idx[a]
        nest_idx[a] = nest_idx[b]
        nest_idx[b] = tmp_nest_idx

    elif query[0] == 3:
        a = query[1]
        print(idx_nest[pigeon_idx[a]])
# 文字のコピーには時間がかかる

n, q = map(int, input().split())

pc = [-1] * (n + 1)
str_list = []


for i in range(q):
    query = list(input().split())
    # pc[p] -> pc[0]
    if query[0] == "1":
        p = int(query[1])
        pc[p] = pc[0]
    
    # pc[p] += s
    elif query[0] == "2":
        p = int(query[1])
        s = query[2]

        if pc[p] == -1:
            str_list.append([-1, s])
        else:
            str_list.append([pc[p], s])

        pc[p] = len(str_list) - 1
    
    # pc[0] -> pc[p]
    elif query[0] == "3":
        p = int(query[1])
        pc[0] = pc[p]

if pc[0] == -1:
    print()
else:
    parts = []
    idx = pc[0]
    while idx != -1:
        parts.append(str_list[idx][1])
        idx = str_list[idx][0]
    print(''.join(reversed(parts)))


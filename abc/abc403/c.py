n, m, q = map(int, input().split())
query = [None] * q

for i in range(q):
    query[i] = list(map(int, input().split()))

user_page = set()
user_all_page = set()

for i in range(q):
    if query[i][0] == 1:
        user_page.add((query[i][1], query[i][2]))
    elif query[i][0] == 2:
        user_all_page.add(query[i][1])
    else:
        x, y = query[i][1], query[i][2]
        if x in user_all_page:
            print('Yes')
        elif (x, y) in user_page:
            print('Yes')
        else:
            print('No')
n, m = map(int, input().split())
c = list(map(int, input().split()))
k = []
a = []
for i in range(m):
    tmp = list(map(int, input().split()))
    k.append(tmp[0])
    a.append(tmp[1:])

zoo = [[] for _ in range(n)]

for i in range(m):
    for j in range(k[i]):
        zoo[a[i][j]-1].append(i)

min_cost = 10 ** 18

for i in range(3**n):
    visits = [0] * n
    cost = 0
    tmp_i = i

    for j in range(n):
        visit_cnt = tmp_i % 3
        visits[j] = visit_cnt
        cost += visit_cnt * c[j]
        tmp_i //= 3
    
    animal_cnt = [0] * m
    for j in range(n):
        if visits[j] > 0:
            for k in zoo[j]:
                animal_cnt[k] += visits[j]

    flg = True
    for i in range(m):
        if animal_cnt[i] < 2:
            flg = False
            break
    
    if flg:
        min_cost = min(min_cost, cost)

print(min_cost)
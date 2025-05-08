n, m = map(int, input().split())

menu = [[] for _ in range(n+1)]

for i in range(m):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    a = tmp[1:]
    for j in range(k):
        menu[a[j]].append(i)

b = list(map(int, input().split()))

ans = []
cant_eat_menu = [False] * m
cant_eat_count = 0

for i in reversed(range(n)):
    ans.append(m - cant_eat_count)
    
    for menu_id in menu[b[i]]:
        if not cant_eat_menu[menu_id]:
            cant_eat_menu[menu_id] = True
            cant_eat_count += 1

ans.reverse()
print(*ans, sep='\n')
n, q = map(int, input().split())

version = [1] * (n + 1)
most_old_version = 1

for i in range(q):
    x, y = map(int, input().split())
    
    if x < most_old_version:
        print(0)
        continue
    
    upgrade_cnt = 0
    for i in range(most_old_version, x+1):
        upgrade_cnt += version[i]
    
    print(upgrade_cnt)
    version[y] += upgrade_cnt
    most_old_version = x + 1

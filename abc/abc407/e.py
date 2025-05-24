# WA

from heapq import heappop, heappush
t = int(input())
for i in range(t):
    n = int(input())
    a = []
    balance = 0
    ans = 0
    for j in range(2 * n):
        ai = int(input())
        if j == 2 * n - 1:
            break
            
        ans += ai
        if j == 0:
            balance += 1
            continue
        
        if balance < 2 * n - j:
            heappush(a, ai)
            balance += 1
        else:
            ans -= heappop(a)
            balance -= 1
    print(ans)

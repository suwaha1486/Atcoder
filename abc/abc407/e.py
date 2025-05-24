# Model Solution

from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(2 * n):
        a.append(int(input()))
    
    # 最大ヒープをシミュレートするために、値を負にして最小ヒープを使用
    heap = []
    ans = 0
    
    for i in range(n):
        if i == 0:
            heappush(heap, -a[0])  # 最初の要素を追加
        else:
            # 2つの要素を追加
            heappush(heap, -a[2*i-1])
            heappush(heap, -a[2*i])
        
        # 最大値（負の値の最小値）を取り出して合計に加算
        v = -heappop(heap)
        ans += v
    
    print(ans)

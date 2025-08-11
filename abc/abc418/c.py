import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

cumsum = [0]
for i in range(n):
    cumsum.append(cumsum[i] + a[i])


for i in range(q):
    b = int(input())
    if b > a[n-1]:
        print(-1)
        continue
    
    # 二分探索と累積和を使って高速化
    idx = bisect.bisect_left(a, b)
    # a[0] ~ a[idx-1] < b, それぞれa[i]を足す
    # a[idx] ~ a[n-1] >= b, それぞれb-1を足す
    ans = cumsum[idx] + (n - idx) * (b - 1)

    ans += 1 
    print(ans)
        

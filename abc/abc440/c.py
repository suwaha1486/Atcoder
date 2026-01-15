t = int(input())

for _ in range(t):
    n, w = map(int, input().split())
    c = list(map(int, input().split()))
    
    m = 2 * w
    s = [0] * m
    for i in range(n):
        s[i % m] += c[i]
    
    cur_sum = sum(s[:w])
    ans = cur_sum
    ss = s + s

    for i in range(m):
        cur_sum += ss[i + w] - ss[i]
        ans = min(ans, cur_sum)
    
    print(ans)
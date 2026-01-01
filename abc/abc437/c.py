t = int(input())

# ソリに載せるトナカイ数最大を求める　⇒　貪欲法？
# W+P小さい順にソート

for _ in range(t):
    n = int(input())
    ans = 0
    tonakai = []
    power_total = 0
    for i in range(n):
        w, p = map(int, input().split())
        power_total += p
        tonakai.append((w, p))
    
    tonakai.sort(key=lambda x: x[0] + x[1])

    for w, p in tonakai:
        if power_total - (w + p) < 0:
            break
        power_total -= (w + p)
        ans += 1

    print(ans)
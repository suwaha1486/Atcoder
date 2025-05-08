n, m = map(int, input().split())

# give up
# 余事象＝直線が平行
# ABの傾き＝(A+B) % N

slope = dict()

for i in range(m):
    a, b = map(int, input().split())
    if slope.get((a+b) % n) is None:
        slope[(a+b) % n] = 1
    else:
        slope[(a+b) % n] += 1

ans = m * (m-1) // 2

for i in slope.values():
    ans -= i * (i-1) // 2

print(ans)
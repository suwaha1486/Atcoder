from collections import defaultdict
import bisect

N, L, R = map(int, input().split())
S = input()

alphabet = defaultdict(list)

for i in range(N):
    alphabet[S[i]].append(i)

# Si = Sj かつ i + L <= j <= i + Rとなるjの個数を数える

ans = 0

for key, value in alphabet.items():
    for i in range(len(value)):
        left = value[i] + L
        right = value[i] + R
        lidx = bisect.bisect_left(value, left, i + 1)
        ridx = bisect.bisect_right(value, right, i + 1)
        ans += ridx - lidx


print(ans)
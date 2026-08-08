from collections import Counter

N = int(input())
C = list(map(int, input().split()))

ans = N - max(Counter(C).values())
print(ans)
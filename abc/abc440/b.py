n = int(input())
t = list(map(int, input().split()))

ans = sorted(range(n), key=lambda i: t[i])

print(*(i + 1 for i in ans[:3]))
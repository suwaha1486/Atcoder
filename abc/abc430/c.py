n, a, b = map(int, input().split())
s = input()

cusum_a = [0] * (n+1)
cusum_b = [0] * (n+1)

for i in range(n):
    if s[i] == 'a':
        cusum_a[i+1] = cusum_a[i] + 1
    else:
        cusum_a[i+1] = cusum_a[i]
    if s[i] == 'b':
        cusum_b[i+1] = cusum_b[i] + 1
    else:
        cusum_b[i+1] = cusum_b[i]

ans = 0
right_A = 0
right_B = 0

for left in range(n):
    if right_A < left + 1:
        right_A = left + 1
    if right_B < left + 1:
        right_B = left + 1

    while right_A <= n and cusum_a[right_A] - cusum_a[left] < a:
        right_A += 1
    while right_B <= n and cusum_b[right_B] - cusum_b[left] < b:
        right_B += 1
    
    if right_A <= n:
        upper = min(right_B, n + 1)
        if right_A < upper:
            ans += upper - right_A

print(ans)
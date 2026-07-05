X, Y, L, R, A, B = map(int, input().split())

total = 0

# [A, B) と [L, R) の重なりを計算
start = max(A, L)
end = min(B, R)

if start < end:
    total += (end - start) * X

if A < L:
    total += (min(B, L) - A) * Y
if B > R:
    total += (B - max(A, R)) * Y

print(total)

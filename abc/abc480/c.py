N, K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# お湯が終わる時刻
end = 0

ans = 0

for i in range(N):
    if A[i] > T:
        break
    if A[i] > end:
        len_not_shower = A[i] - end
        # 小数点以下切り上げ計算
        ans += (len_not_shower + K - 1) // K

    end = A[i] + K

if end < T:
    len_not_shower = T - end
    ans += (len_not_shower + K - 1) // K

print(ans)
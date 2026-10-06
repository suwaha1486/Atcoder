Q = int(input())
S = input()
T = input()
S_len = len(S)
T_len = len(T)

# Sの中でTの部分文字列の開始位置を記録
# その後，累積和を取ることで，部分文字列の出現回数を求める
prefix_sum = [0] * (S_len + 1)
for i in range(S_len):
    if S[i:i+T_len] == T:
        prefix_sum[i + 1] = prefix_sum[i] + 1
    else:
        prefix_sum[i + 1] = prefix_sum[i]

# 累積和を取ることで，部分文字列の出現回数を求める
for _ in range(Q):
    L, R = map(int, input().split())
    if R - L + 1 < T_len:
        print("No")
        continue
    
    cnt = prefix_sum[R - T_len + 1] - prefix_sum[L - 1]
    if cnt > 0:
        print("Yes")
    else:
        print("No")

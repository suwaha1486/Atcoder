n, k = map(int, input().split())
s = list(input())

cnt1 = 0
flg1 = False
cnt_k1 = 0

for i in range(n):
    if s[i] == '1':
        if not flg1:
            flg1 = True
            cnt1 += 1
        if cnt1 == k:
            cnt_k1 += 1
            s[i] = 0
    elif s[i] == '0':
        if flg1 and cnt1 == k - 1:
            start_idx = i
        flg1 = False


for i in range(start_idx, start_idx + cnt_k1):
    s[i] = 1

print(*s, sep="")
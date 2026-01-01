n, m = map(int, input().split())
s = input()
t = input()

ans = 10**9
for i in range(0, n-m+1):
    tmp_ans = 0
    for j in range(m):
        s_num = int(s[i+j])
        t_num = int(t[j])

        if s_num < t_num:
            s_num += 10

        tmp_ans += s_num - t_num

    ans = min(ans, tmp_ans)

print(ans)
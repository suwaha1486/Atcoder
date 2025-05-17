n = int(input())
p = list(map(int, input().split()))


l_increasing_len = [0] * n
l_increasing_len[0] = 1
for i in range(1, n):
    if p[i-1] < p[i]:
        l_increasing_len[i] = l_increasing_len[i-1] + 1
    else:
        l_increasing_len[i] = 1

r_increasing_len = [0] * n
r_increasing_len[n-1] = 1
for i in range(n-2, -1, -1):
    if p[i] < p[i+1]:
        r_increasing_len[i] = r_increasing_len[i+1] + 1
    else:
        r_increasing_len[i] = 1

ans = 0
for k in range(1, n - 1):
    if not (p[k-1] < p[k] and p[k] > p[k+1]):
        continue

    num_s_choices = l_increasing_len[k] - 1
    if num_s_choices < 1:
        continue

    for m in range(k + 1, n - 1):
        if m > k + 1 and p[m-1] <= p[m]:
            break 
        
        if p[m-1] > p[m] and p[m] < p[m+1]:
            num_t_choices = r_increasing_len[m] - 1
            if num_t_choices < 1:
                continue
            
            ans += num_s_choices * num_t_choices
print(ans)
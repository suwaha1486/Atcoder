s = input()
n = len(s)

def filling_rate(i, j):
    if s[i] == 't' and s[j] == 't' and j - i + 1 >= 3:
        length = j - i + 1
        t_count = s[i:j+1].count('t')
        if t_count >= 2:
            return (t_count - 2) / (length - 2)
    return 0

ans = 0
for i in range(n - 2):
    for j in range(i + 2, n):
        ans = max(ans, filling_rate(i, j))

print(ans)

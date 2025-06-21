s = list(input())

cnt0 = 0
n = len(s)
i = 0
while i < n-1:
    if s[i] == '0' and s[i+1] == '0':
        cnt0 += 1
        i += 2
    else:
        i += 1

print(n - cnt0)
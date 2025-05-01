s = list(input())

n = len(s)

if n == 1:
    print(*s)
    exit()


pos = 0
while pos < n-1:
    if s[pos] == 'W' and s[pos+1] == 'A':
        s[pos] = 'A'
        s[pos+1] = 'C'
        pos = max(0, pos-1)
    else:
        pos += 1

print(*s, sep='')
s = input()

ans = 0
n = len(s)

for i in range((n-3)//2 + 1):
    for j in range(n-(3+2*i)+1):
        if s[j] == 'A' and s[j+i+1] == 'B' and s[j+2*i+2] == 'C':
            ans += 1

print(ans)
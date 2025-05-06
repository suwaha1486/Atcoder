n = int(input())

c = []

for i in range(n):
    a = list(map(int, input().split()))
    c.append(a)

row = []
col = []
for i in range(n):
    row.append(sum(c[i]))
    col.append(sum(c[j][i] for j in range(n))) 

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if row[i] > row[j]:
            ans += 1
        if col[i] > col[j]:
            ans += 1
            
print(ans)
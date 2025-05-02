x = int(input())

ans = 1
i = 1
while i < x:
    ans += 1
    i *= ans

print(ans)
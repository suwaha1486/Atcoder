s = input()

ans = []
cnt = 0
for i in range(len(s)):
    if s[i] == "|":
        ans.append(cnt)
        cnt = 0
    elif s[i] == "-":
        cnt += 1
    
print(*ans[1:], sep=" ")
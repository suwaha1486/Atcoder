n = int(input())
s = input()

ans = 1
i = 0
while i < n:
    # '1'の連続をカウント
    if s[i] != '1':
        i += 1
        continue
        
    length1 = 0
    while i < n and s[i] == '1':
        length1 += 1
        i += 1
    
    # '/'がなければ次の文字へ
    if i >= n or s[i] != '/':
        i += 1
        continue
    
    i += 1  # '/'をスキップ
    
    # '2'の連続をカウント
    if i >= n or s[i] != '2':
        continue
        
    length2 = 0
    while i < n and s[i] == '2':
        length2 += 1
        i += 1
        
    ans = max(ans, min(length1, length2) * 2 + 1)

print(ans)
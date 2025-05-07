# ごり押し

s = list(input())

cnt = 0
while True:
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == 'o':
            s.insert(i, '0')
            cnt += 1
            break
        elif i % 2 == 1 and s[i] == 'i':
            s.insert(i, '1')
            cnt += 1
            break
    
    else:
        break

if len(s) % 2 == 0:
    print(cnt)
else:
    print(cnt + 1)
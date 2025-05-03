n = int(input())
s = input()

if n % 2 == 0:
    print('No')
    exit()

for i in range(n):
    if i < (n-1) // 2 and s[i] == '1':
        continue
    elif i == (n-1) // 2 and s[i] == '/':
        continue
    elif i > (n-1) // 2 and s[i] == '2':
        continue
    else:
        print('No')
        exit()

print('Yes')
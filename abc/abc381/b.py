s = input()

n = len(s)

if n % 2 == 1:
    print('No')
    exit()

moji = set()

for i in range(n // 2):
    if s[2*i] == s[2*i+1]:
        if s[2*i] in moji:
            print('No')
            exit()
        else:
            moji.add(s[2*i])
    else:
        print('No')
        exit()

print('Yes')
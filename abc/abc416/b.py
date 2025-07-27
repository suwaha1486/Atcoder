s = input()

t = ''
sharp_flg = True

for i in range(len(s)):
    if s[i] == '#':
        t += '#'
        sharp_flg = True
    elif s[i] == '.':
        if sharp_flg:
            t += 'o'
            sharp_flg = False
        else:
            t += '.'

print(t)

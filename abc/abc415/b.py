s = input()

souko = []
for i in range(len(s)):
    if s[i] == '#':
        souko.append(i+1)
        if len(souko) == 2:
            print(souko[0],',',souko[1], sep='')
            souko.clear()

t = input()
u = input()

for i in range(len(t)-len(u)+1):
    for j in range(len(u)):
        if not(t[i+j] == u[j] or t[i+j] == '?'):
            break
        if j == len(u)-1:
            print('Yes')
            exit()

print('No')
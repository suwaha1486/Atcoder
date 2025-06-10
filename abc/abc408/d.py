# give up
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    c = [0] * (n + 1)
    for i in range(n):
        if s[i] == '0':
            c[i + 1] = c[i] + 1
        else:
            c[i + 1] = c[i] - 1
    
    ones = s.count('1')

    ma = 0
    res = 0 
    
    for i in range(n + 1):
        res = min(res, c[i] - ma)
        ma = max(ma, c[i])
            
    print(ones + res)

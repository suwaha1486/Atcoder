n = int(input())

a = ['-'] * n

if n % 2 == 0:
    a[n//2-1] = '='
    a[n//2] = '='

else:
    a[n//2] = '='

print(*a, sep='')
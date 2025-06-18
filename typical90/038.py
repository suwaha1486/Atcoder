# ★3
a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


ans = a * b // gcd(a, b)
if ans > 10**18:
    print('Large')
else:
    print(ans)

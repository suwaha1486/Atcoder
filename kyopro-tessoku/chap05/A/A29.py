def mod_pow(x, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x % mod
        x = x * x % mod
        n //= 2
    return result

a, b = map(int, input().split())
m = 1000000007
print(mod_pow(a, b, m))

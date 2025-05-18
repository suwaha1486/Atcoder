def mod_pow(x, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x % mod
        x = x * x % mod
        n //= 2
    return result

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7

    if n == 1:
        print(k)
        exit()
    if k == 1:
        print(0)
        exit()
    if n == 2:
        print(k * (k-1) % mod)
        exit()
    if k == 2:
        print(0)
        exit()

    ans = k
    ans *= (k-1)
    ans *= mod_pow(k-2, n-2, mod)
    print(ans % mod)

if __name__ == "__main__":
    main()

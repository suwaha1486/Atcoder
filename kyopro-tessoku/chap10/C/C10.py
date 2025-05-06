def power(a, b, mod):
    ans = 1
    for i in range(70):
        wari = 2 ** i
        if b // wari % 2 == 1:
            ans = ans * a % mod
        a = a * a % mod
    return ans

def main():
    # 1列目12通り, 2列目以降7通り
    # 12 * 7^(w-1)

    w = int(input())

    MOD = 10 ** 9 + 7

    power7 = power(7, w - 1, MOD)
    ans = 12 * power7 % MOD
    
    print(ans)

if __name__ == "__main__":
    main()
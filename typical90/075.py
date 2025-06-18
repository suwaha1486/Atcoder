# ★3
n = int(input())

def count_prime_factors(num):
    count = 0
    for i in range(2, int(num ** 0.5) + 2):
        while num % i == 0:
            count += 1
            num //= i
    if num > 1:
        count += 1
    return count

prime_factors = count_prime_factors(n)

if prime_factors == 0:
    print(0)
    exit()

ans = 0
while 2 ** ans < prime_factors:
    ans += 1

print(ans)

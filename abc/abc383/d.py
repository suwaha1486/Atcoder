n = int(input())

# 正の約数がちょうど9個 → 平方数 * 平方数 or x ^ 8

if n < (2 ** 2) * (3 ** 2):
    print(0)
    exit()

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes
            
primes = eratosthenes(int(n ** 0.5) // 2)

ans = 0
for i in range(len(primes)):
    if primes[i] ** 8 <= n:
        ans += 1
    for j in range(i + 1, len(primes)):
        if primes[i] * primes[i] * primes[j] * primes[j] <= n:
            ans += 1
        else:
            break

print(ans)
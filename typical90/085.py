# 全探索
k = int(input())

prime_factor = set()
for i in range(1, int(k ** 0.5) + 1):
    if k % i == 0:
        prime_factor.add(i)
        prime_factor.add(k // i)

prime_factors = sorted(prime_factor)

cnt = 0
for i in range(len(prime_factors)):
    for j in range(i, len(prime_factors)):
        a = prime_factors[i]
        b = prime_factors[j]
        if k % (a * b) == 0:
            c = k // (a * b)
            if a <= b <= c:
                cnt += 1

print(cnt)

n = int(input())

divisors = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)

divisors.sort()
for d in divisors:
    print(d)
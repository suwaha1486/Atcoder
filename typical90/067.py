# ★2
n, k = input().split()
k = int(k)

for _ in range(k):
    n_10 = 0
    for i in range(len(n)):
        ni = int(n[i])
        n_10 += ni * (8 ** (len(n) - i - 1))

    n_9 = ""
    if n_10 == 0:
        n_9 = "0"
    else:
        while n_10 > 0:
            num = n_10 % 9
            if num == 8:
                num = 5
            n_9 = str(num) + n_9
            n_10 //= 9

    n = n_9

print(n)

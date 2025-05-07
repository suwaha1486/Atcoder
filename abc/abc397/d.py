# give up

def solve_quadratic(a, b, c):
    # ax^2 + bx + c = 0 の整数解を求める
    l, r = 0, 600000001
    while r - l > 1:
        mid = (l + r) // 2
        if a * mid * mid + b * mid + c <= 0:
            l = mid
        else:
            r = mid
    if a * l * l + b * l + c == 0:
        return l
    return -1

n = int(input())
for d in range(1, int(n ** (1/3)) + 2):
    if n % d != 0:
        continue
    m = n // d  # = 3*k^2 + 3*d*k + d^2
    k = solve_quadratic(3, 3 * d, d * d - m)
    if k > 0:
        print(k + d, k)
        exit()
print(-1)
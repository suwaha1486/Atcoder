# ★2
a, b, c = map(int, input().split())

def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclid_gcd(b, a % b)

cube_length = euclid_gcd(a, euclid_gcd(b, c))

ans = (a // cube_length - 1)  +  (b // cube_length - 1) + (c // cube_length - 1)

print(ans)

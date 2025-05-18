n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_mod = {}
b_mod = {}
c_mod = {}

for i in range(n):
    a_mod[a[i] % 46] = a_mod.get(a[i] % 46, 0) + 1
    b_mod[b[i] % 46] = b_mod.get(b[i] % 46, 0) + 1
    c_mod[c[i] % 46] = c_mod.get(c[i] % 46, 0) + 1


ans = 0
for i in a_mod:
    for j in b_mod:
        for k in c_mod:
            if (i + j + k) % 46 == 0:
                ans += a_mod[i] * b_mod[j] * c_mod[k]

print(ans)

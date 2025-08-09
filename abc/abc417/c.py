from collections import Counter

n = int(input())
a = list(map(int, input().split()))

# j-i = a[i] + a[j]
# a[i] + i = j - a[j]

b = []
c = []
for i in range(n):
    b.append(a[i] + i)
    c.append(i - a[i])
    
b_counter = Counter(b)
c_counter = Counter(c)

ans = 0
for key in b_counter.keys():
    ans += b_counter[key] * c_counter[key]

print(ans)

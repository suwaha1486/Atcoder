n, m = map(int, input().split())
b = list(map(int, input().split()))
w = list(map(int, input().split()))

b.sort(reverse=True)
w.sort(reverse=True)

value_sum = 0
w_idx = 0

for i in range(n):
    if b[i] > 0:
        value_sum += b[i]

        if w_idx < m and w[w_idx] > 0:
            value_sum += w[w_idx]
            w_idx += 1
            
    elif w_idx < m and b[i] + w[w_idx] > 0:
        value_sum += b[i] + w[w_idx]
        w_idx += 1

print(value_sum)
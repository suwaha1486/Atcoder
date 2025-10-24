from collections import defaultdict

n, k = map(int, input().split())
s = input()

len_k_str = defaultdict(int)

for i in range(n-k+1):
    len_k_str[s[i:i+k]] += 1

max_value = max(len_k_str.values())
print(max_value)

ans = []

for key, value in len_k_str.items():
    if value == max_value:
        ans.append(key)

ans.sort()
print(*ans, sep=' ')
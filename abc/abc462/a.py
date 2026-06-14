S = list(input())

num_set = set()
for i in range(10):
    num_set.add(str(i))

ans_str = ''
for c in S:
    if c in num_set:
        ans_str += c

print(ans_str)
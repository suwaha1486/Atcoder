n = int(input())
a = list(map(int, input().split()))

second_dict = dict()

for i in range(n):
    if second_dict.get(a[i]) is None:
        second_dict[a[i]] = 1
    else:
        second_dict[a[i]] += 1

first_set = set()
second_len = len(second_dict)
ans = 0

for i in range(n):
    first_set.add(a[i])
    first_len = len(first_set)
    second_dict[a[i]] -= 1
    if second_dict[a[i]] == 0:
        second_len -= 1
        
    ans = max(ans, second_len + first_len)

print(ans)
n = int(input())
a = list(map(int, input().split()))

all_num_set = set(range(1, n+1))
num_set = set()

for i in range(n):
    if a[i] != -1:
        if a[i] in num_set:
            print('No')
            exit()
        else:
            num_set.add(a[i])

removed_num_set = all_num_set - num_set

for i in range(n):
    if a[i] == -1:
        a[i] = removed_num_set.pop()

print('Yes')
print(*a, sep=' ')
n, m = map(int, input().split())
a = list(map(int, input().split()))

num_list = [0] * m
for i in range(n):
    num_list[a[i]-1] += 1

for i in range(m):
    if num_list[i] == 0:
        print(0)
        exit()

for i in range(n-1, -1, -1):
    if num_list[a[i]-1] == 1:
        print(n-i)
        exit()
    else:
        num_list[a[i]-1] -= 1
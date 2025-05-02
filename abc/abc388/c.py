n = int(input())
a = list(map(int, input().split()))

cnt = 0
j = 1
for i in range(n-1):
    while j < n and 2 * a[i] > a[j]:
    	j += 1
    cnt += n-j

print(cnt)
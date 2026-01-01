n = int(input())
a = list(map(int, input().split()))

ans = 0

for left in range(n):
    for right in range(left + 1, n):
        a_lr = sum(a[left:right+1])

        for k in range(left, right + 1):
            if a_lr % a[k] == 0:
                break
        else:
            ans += 1

print(ans)
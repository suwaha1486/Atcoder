n, m = map(int, input().split())

m %= 10
if m == 0:
    m = 10

num_list = [[1] * n]

tmp = [1] * n
# whileループを抜ける条件を変更
while sum(tmp) < m*n:
    for i in reversed(range(n)):
       if tmp[i] != m:
            break
    tmp[i:] = [tmp[i] + 1] * (n-i)
    num_list.append(tmp[:])

print(len(num_list))
for num in num_list:
    for i in range(n):
        num[i] += 10 * i
    print(*num, sep=' ')
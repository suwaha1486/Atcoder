n, m = map(int, input().split())

m %= 10
if m == 0:
    m = 10

'''
なぜか31問中2問TLEになる
num_list = [[1] * n]

tmp = [1] * n
while True:
    for i in reversed(range(n)):
       if tmp[i] != m:
            break
    tmp[i:] = [tmp[i] + 1] * (n-i)
    
    num_list.append(tmp[:])

    if all(x == m for x in tmp):
        break

print(len(num_list))
for num in num_list:
    for i in range(n):
        num[i] += 10 * i
    print(*num, sep=' ')
'''

from itertools import combinations_with_replacement
num_list = list(combinations_with_replacement(range(1,m+1), n))

print(len(num_list))
for num in num_list:
    pre = 0
    tmp = []
    for j in num:
        tmp.append(j+pre)
        pre += 10
    print(*tmp)
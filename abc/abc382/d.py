import itertools

n, m = map(int, input().split())

num_list = []

for i in range(m):
    num_list.append(i+1)

answer = []
cnt = 0

for pair in itertools.combinations(num_list, n):
    a_pre = pair[0]
    flg = True
    for i in range(1, n):
        if pair[i] - a_pre < 10:
            flg = False
            break
        else:
            a_pre = pair[i]

    if flg:
        answer.append(pair)
        cnt += 1

print(cnt)
for ans in answer:
    print(*ans, sep=' ')
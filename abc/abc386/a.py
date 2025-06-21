from collections import Counter

card = list(map(int, input().split()))

cnt = Counter(card)

if len(cnt) == 1:
    print('No')
    exit()

d = cnt.most_common(2)

if d[0][1] == 3 and d[1][1] == 1:
    print('Yes')
elif d[0][1] == 2 and d[1][1] == 2:
    print('Yes')
else:
    print('No')
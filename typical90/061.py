q = int(input())

card = []

for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        card.insert(0, x)
    elif t == 2:
        card.append(x)
    else:
        print(card[x-1])

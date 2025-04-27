a = list(map(int, input().split()))

card = [0] * 13
for i in range(7):
    card[a[i] - 1] += 1

card.sort(reverse=True)

if card[0] >= 3 and card[1] >= 2:
    print('Yes')
else:
    print('No')
from collections import defaultdict

dice1 = defaultdict(int)
dice2 = defaultdict(int)
dice3 = defaultdict(int)

tmp = list(map(int, input().split()))

for i in range(len(tmp)):
    dice1[tmp[i]] += 1

tmp = list(map(int, input().split()))
for i in range(len(tmp)):
    dice2[tmp[i]] += 1

tmp = list(map(int, input().split()))
for i in range(len(tmp)):
    dice3[tmp[i]] += 1

combination = 0

combination += dice1[4] * dice2[5] * dice3[6]
combination += dice1[5] * dice2[4] * dice3[6]
combination += dice1[6] * dice2[4] * dice3[5]
combination += dice1[4] * dice2[6] * dice3[5]
combination += dice1[5] * dice2[6] * dice3[4]
combination += dice1[6] * dice2[5] * dice3[4]

print(combination / 6 ** 3)
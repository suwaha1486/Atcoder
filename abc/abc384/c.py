point = list(map(int, input().split()))

score = []

for bit in range(1, 32):
    solved_point = 0
    name = ''
    for digit in range(5):
        # 0ならFalse，1以上ならTrue
        if bit & (1 << digit):
            solved_point += point[digit]
            name += 'ABCDE'[digit]

    score.append((solved_point, name))

# 辞書順並び替え
score.sort(key=lambda x: (-x[0], x[1]))

for i in range(31):
    print(score[i][1])
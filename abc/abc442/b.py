Q = int(input())

music_play =False
music_volume = 0

for _ in range(Q):
    A = int(input())
    if A == 1:
        music_volume += 1
    elif A == 2:
        music_volume = max(0, music_volume - 1)
    elif A == 3:
        music_play = not music_play

    if music_play and music_volume >= 3:
        print('Yes')
    else:
        print('No')
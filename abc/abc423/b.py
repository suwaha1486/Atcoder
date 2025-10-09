n = int(input())
l = list(map(int, input().split()))

possible_room = [False] * (n + 1)
possible_room[0] = True
possible_room[n] = True

for i in range(n):
    if l[i] == 1:
        break
    possible_room[i+1] = True

for i in range(n-1, -1, -1):
    if l[i] == 1:
        break
    possible_room[i] = True

print(possible_room.count(False))
a = list(map(int, input().split()))
correct_a = [1, 2, 3, 4, 5]

cnt = 0
pos = []
for i in range(5):
    if a[i] == correct_a[i]:
        continue
    else:
        cnt += 1
        pos.append(i)

if cnt == 2 and pos[1] - pos[0] == 1:
    print("Yes")
else:
    print("No")
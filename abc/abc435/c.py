n = int(input())
a = list(map(int, input().split()))

# [i, possible_pos) の範囲ではドミノ倒せる
possible_pos = a[0]

for i in range(1, n):
    if i > possible_pos - 1:
        break
    possible_pos = max(possible_pos, (i + a[i]))

print(min(possible_pos, n))
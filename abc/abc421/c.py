n = int(input())
s = input()

A_cnt = 0
B_cnt = 0
A_pos = 0
B_pos = 0

for i in range(2 * n):
    if s[i] == 'A':
        A_cnt += abs(i - A_pos)
        A_pos += 2
    else:
        B_cnt += abs(i - B_pos)
        B_pos += 2

print(min(A_cnt, B_cnt))
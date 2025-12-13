s = input()

first_half_len = 0
second_half_len = 0
first_half_num = -100
second_half_num = int(s[0])

ans = 0

for i in range(len(s)):
    num = int(s[i])
    if num == second_half_num:
        second_half_len += 1
    else:
        if first_half_num + 1 == second_half_num:
            ans += min(first_half_len, second_half_len)
        first_half_len = second_half_len
        first_half_num = second_half_num
        second_half_len = 1
        second_half_num = num

if first_half_num + 1 == second_half_num:
    ans += min(first_half_len, second_half_len)

print(ans)
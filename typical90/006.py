# ★5
n, k = map(int, input().split())
s = input()

ans_str = ""

start_pos = 0
for i in range(k):
    min_ascii_num = 123
    min_ascii_pos = 0
    for j in range(start_pos, n-k+i+1):
        ascii_num = ord(s[j])
        if ascii_num < min_ascii_num:
            min_ascii_num = ascii_num
            min_ascii_pos = j
    ans_str += chr(min_ascii_num)
    start_pos = min_ascii_pos+1

print(ans_str)
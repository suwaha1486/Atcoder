n = int(input())

str_len = 0
ans_str = ""

for i in range(n):
    c, l = input().split()
    l = int(l)
    if str_len + l > 100:
        print('Too Long')
        exit()
    str_len += l
    ans_str += c * l

print(ans_str)

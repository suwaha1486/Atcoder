# 制約より10進数で回文チェック全て行うとTLE
# 回文を生成してからn進数で回文チェック
# 回文は半分の桁で済むことがポイント

a = int(input())
n = int(input())

# 10進数をn進数に変換
def base_10_to_n(x, n):
    str_n = ""
    while x > 0:
        str_n = str(x % n) + str_n
        x //= n
    return str_n


digit = len(str(n))

ans = 0

for length in range(1, digit + 1):
    half_len = (length + 1) // 2
    if length > 1:
        start = 10 ** (half_len - 1)
    else:
        start = 1
    end = 10 ** half_len

    for i in range(start, end):
        s = str(i)
        if length % 2 == 0:
            num = int(s + s[::-1])
        else:
            num = int(s + s[:-1][::-1])
        if num > n:
            break
        change_num = base_10_to_n(num, a)
        if change_num == change_num[::-1]:
            ans += num

print(ans)

# gpt作

from itertools import permutations

S = input()

# Sに出てくる文字を重複なしで取り出す
chars = list(dict.fromkeys(S))
K = len(chars)


def is_prime(n):
    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True


# K個の異なる数字の割り当てを全探索
for digits in permutations(range(10), K):

    # 文字 -> 数字 の対応表
    mp = {}

    for i in range(K):
        mp[chars[i]] = digits[i]

    # 先頭が0ならダメ
    if mp[S[0]] == 0:
        continue

    # Sを数字に変換
    num = 0

    for c in S:
        num = num * 10 + mp[c]

    # 素数なら終了
    if is_prime(num):
        print(num)
        exit()

print(-1)
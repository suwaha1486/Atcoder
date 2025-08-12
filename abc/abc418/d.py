n = int(input())
s = input()

'''
0の個数の変化
00 -> 1：-2
01 -> 0：0
10 -> 0：0
11 -> 1：0

部分文字列で「0の個数が偶数」の場合美しい文字列となる

dp_even[i]: i文字目までの0の個数が偶数の文字列の個数
dp_odd[i]: i文字目までの0の個数が奇数の文字列の個数
'''

dp_even = [0] * (n+1)
dp_odd = [0] * (n+1)

for i in range(n):
    # 0の個数が増える
    if s[i] == '0':
        # ex. 11 -> 110
        dp_even[i+1] = dp_odd[i] 
        dp_odd[i+1] = dp_even[i] + 1

    # 1の個数が増える = 0の個数は変わらない
    elif s[i] == '1':
        # ex. 00 -> 001
        dp_even[i+1] = dp_even[i] + 1
        dp_odd[i+1] = dp_odd[i]

print(sum(dp_even))

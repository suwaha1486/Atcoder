N = int(input())
A = list(map(int, input().split()))

coin_cnt_100 = 0
coin_cnt_10 = 0
coin_cnt_1 = 0
for i in range(N):
    money = (1000 - A[i] % 1000) % 1000
    coin_cnt_100 += money // 100
    money %= 100
    coin_cnt_10 += money // 10
    money %= 10
    coin_cnt_1 += money

print(coin_cnt_1, coin_cnt_10, coin_cnt_100)
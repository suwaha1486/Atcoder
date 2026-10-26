Q = int(input())

bank = {}

bank_cnt = 1
for _ in range(Q):
    query = input()
    if query in bank:
        print(bank[query])
    else:
        bank[query] = bank_cnt
        print(bank_cnt)
        bank_cnt += 1
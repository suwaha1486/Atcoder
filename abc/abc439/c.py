n = int(input())

max_num = int(n ** 0.5)

Squared_num = []
for i in range(1, max_num + 1):
    Squared_num.append(i ** 2)

ans_set = set()
wrong_set = set()
for i in range(len(Squared_num)):
    for j in range(i + 1, len(Squared_num)):
        tmp_num = Squared_num[i] + Squared_num[j]
        if tmp_num <= n:
            if tmp_num in wrong_set:
                continue
            if tmp_num in ans_set:
                wrong_set.add(tmp_num)
                ans_set.remove(tmp_num)
            else:
                ans_set.add(tmp_num)

ans = list(ans_set)
ans.sort()
print(len(ans))
print(*ans)
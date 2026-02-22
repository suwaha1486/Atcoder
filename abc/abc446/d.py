from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
 
# 各値の階段の段数をdefaultdictで管理
stair_dict = defaultdict(int)

for i in range(N):
    if stair_dict[A[i] - 1] > 0:
        stair_dict[A[i]] =  stair_dict[A[i] - 1] + 1
    else:
        stair_dict[A[i]] = 1

print(max(stair_dict.values()))

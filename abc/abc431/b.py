x = int(input())
n = int(input())
w = list(map(int, input().split()))
w_flag = [False] * n
q = int(input())

total_weight = x

for i in range(q):
    p = int(input()) - 1
    if w_flag[p]:
        total_weight -= w[p]
        w_flag[p] = False
    else:
        total_weight += w[p]
        w_flag[p] = True
    print(total_weight)

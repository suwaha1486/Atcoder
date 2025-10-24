q = int(input())

# (: 1, ):-1
# 1: 累積和が0
# 2: 全ての時点での累積和が0以上

stack = [(0, 0)]
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        if query[1] == "(":
            asum_now = stack[-1][0] + 1
            min_sum = min(stack[-1][1], asum_now)
            stack.append((asum_now, min_sum))
        else:
            asum_now = stack[-1][0] - 1
            min_sum = min(stack[-1][1], asum_now)
            stack.append((asum_now, min_sum))
    elif query[0] == "2":
        stack.pop()
    
    if stack[-1][0] == 0 and stack[-1][1] >= 0:
        print("Yes")
    else:
        print("No")
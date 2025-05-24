s = list(input())

a_push = len(s)
b_push = 0

num = [int(c) for c in s]

for i in range(len(num)-1):
    tmp = num[i] - num[i+1]
    if tmp >= 0:
        b_push += tmp
    else:
        b_push += 10 + tmp

print(a_push + b_push + num[len(num)-1])

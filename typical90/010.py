n = int(input())

class1 = [0] * (n + 1)
class2 = [0] * (n + 1)

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        class1[i + 1] = p
    else:
        class2[i + 1] = p

for i in range(1, n + 1):
    class1[i] += class1[i-1]
    class2[i] += class2[i-1]

q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    print(class1[r] - class1[l-1], class2[r] - class2[l-1])
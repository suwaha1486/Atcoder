d = int(input())
x = [int(input())]

for i in range(1, d):
    x.append(x[-1] + int(input()))

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if x[s-1] == x[t-1]:
        print("Same")
    elif x[s-1] < x[t-1]:
        print(t)
    else:
        print(s)
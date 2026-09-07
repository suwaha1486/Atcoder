N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    num = (i // 10) * 10
    if num < P[i] <= num + 10:
        continue
    else:
        print("No")
        exit()
print("Yes")
N = int(input())

r = 1
ans = 0
for i in range(1, N):
    r = max(r, i)
    while r < N:
        print("?", i, r + 1, flush=True)
        judge = input()
        if judge == "Yes":
            r += 1
        else:
            break
    ans += r - i
print("!", ans, flush=True)
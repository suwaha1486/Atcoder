N = int(input())
S = input()

left = []
right = []
rev = False

for i in range(N):
    if rev:
        left.append(i + 1)
    else:
        right.append(i + 1)
    if S[i] == "o":
        rev = not rev

ans = left[::-1] + right
if rev:
    ans = ans[::-1]
print(*ans, sep=" ")
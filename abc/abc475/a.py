S = input()
ans = ""

for i in range(len(S)-1):
    ans += S[i] + "o"

ans += S[-1]
print(ans)

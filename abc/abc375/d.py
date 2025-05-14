s = input()

alphabet = [[] for _ in range(26)]

for i in range(len(s)):
    alphabet[ord(s[i]) - ord('A')].append(i)

ans = 0
for character in alphabet:
    if len(character) <  2:
        continue
    
    cum_sum = [0] * (len(character) + 1)
    for i in range(len(character)):
        cum_sum[i + 1] = cum_sum[i] + character[i]

    for i in range(len(character)):
        ans += i * (character[i] - 1) - cum_sum[i]

print(ans)
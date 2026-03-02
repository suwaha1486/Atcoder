from collections import defaultdict

S = input()

alphabet = defaultdict(int)

for i in range(len(S)):
    alphabet[S[i]] += 1

max_count = max(alphabet.values())
max_alphabet_keys = [k for k, v in alphabet.items() if v == max_count]

ans = ''
for i in range(len(S)):
    if S[i] in max_alphabet_keys:
        continue
    
    ans += S[i]

print(ans)

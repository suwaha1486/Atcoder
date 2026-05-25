from collections import defaultdict
T = int(input())
for _ in range(T):
    S = input()
    N = len(S)
    alphabet_dict = defaultdict(int)
    for i in range(len(S)):
        alphabet_dict[S[i]] += 1
    # Convert dictionary items to a list of [char, count] for mutability
    sorted_alphabet = sorted([[char, count] for char, count in alphabet_dict.items()], key=lambda x: x[1], reverse=True)
    
    if sorted_alphabet[0][1] > N - sorted_alphabet[0][1] + 1:
        print('No')
        continue
    
    ans = [None] * N
    alphabet_idx = 0
    for i in range(0, N, 2):
        ans[i] = sorted_alphabet[alphabet_idx][0]
        sorted_alphabet[alphabet_idx][1] -= 1
        if sorted_alphabet[alphabet_idx][1] == 0:
            alphabet_idx += 1
    for i in range(1, N, 2):
        ans[i] = sorted_alphabet[alphabet_idx][0]
        sorted_alphabet[alphabet_idx][1] -= 1
        if sorted_alphabet[alphabet_idx][1] == 0:
            alphabet_idx += 1
    print('Yes')
    print(''.join(ans))

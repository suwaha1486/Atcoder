from itertools import permutations

x = int(input())

permutations_list = list(permutations(str(x)))

min_num = 10000000
for permutation in permutations_list:
    if permutation[0] == '0':
        continue
    min_num = min(min_num, int(''.join(permutation)))

print(min_num)
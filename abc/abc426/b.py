from collections import Counter

S = input()

counter = Counter(S)

if list(counter.values())[0] == 1:
    print(list(counter.keys())[0])
else:
    print(list(counter.keys())[1])
n = int(input())

name_set = set()

for i in range(n):
    s = input()
    if s in name_set:
        continue
    else:
        print(i + 1)
        name_set.add(s)

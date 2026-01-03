n = int(input())

num_set = set()

while n != 1:
    new_num = 0
    for i in range(len(str(n))):
        new_num += int(str(n)[i]) ** 2
    n = new_num
    if n in num_set:
        print('No')
        exit()
    num_set.add(n)

print('Yes')
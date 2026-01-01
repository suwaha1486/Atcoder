n, m = map(int, input().split())
bird_list = [[] for _ in range(m)]

for i in range(n):
    a, b = map(int, input().split())
    bird_list[a-1].append(b)

for i in range(m):
    print(sum(bird_list[i]) / len(bird_list[i]))

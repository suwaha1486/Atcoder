from collections import defaultdict

N, M = map(int, input().split())

research_list = [N-1] * N

for _ in range(M):
    A, B = map(int, input().split())
    research_list[A-1] -= 1
    research_list[B-1] -= 1

ans_list = [0] * N

for i in range(N):
    if research_list[i] < 3:
        continue

    num_research = research_list[i]
    ans_list[i] = num_research * (num_research - 1) * (num_research - 2) // 6

print(*ans_list, sep=' ')
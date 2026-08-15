import heapq

N = int(input())
A = list(map(int, input().split()))

left_queue = []
right_queue = []

for a in A:
    if a > 0:
        heapq.heappush(right_queue, a)
    else:
        heapq.heappush(left_queue, -a)

pos = 0
step = 0

for _ in range(N):

    if not left_queue:
        next_pos = heapq.heappop(right_queue)

    elif not right_queue:
        next_pos = -heapq.heappop(left_queue)

    else:
        # 左右の次の候補
        left = -left_queue[0]
        right = right_queue[0]

        if pos - left <= right - pos:
            next_pos = -heapq.heappop(left_queue)
        else:
            next_pos = heapq.heappop(right_queue)

    step += abs(next_pos - pos)
    pos = next_pos

print(step)